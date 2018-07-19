import os.path
from functools import reduce

class Member:
    def __init__(self, new_name: str, new_preferences: [str]):
        self.name = new_name
        self.match = None
        self.preferences = new_preferences

class Group:
    def __init__(self):
        self.members = dict()
        
    def add_member(self, new_member: Member) -> None:
        self.members[new_member.name] = new_member

    def get_member_names(self) -> list:
        return sorted(self.members.keys(), reverse=True)

    def get_member_preferences(self, member_name: str) -> [str]:
        return self.members[member_name].preferences

    def set_member_preferences(self, member_name: str, new_preferences: [str]) -> None:
        self.members[member_name].preferences = new_preferences

    def get_member_match(self, member_name: str) -> str:
        return self.members[member_name].match

    def set_member_match(self, member_name: str, match_name: str) -> None:
        self.members[member_name].match = match_name

def join_path(*args) -> str:
    return reduce(lambda x,y: os.path.join(x,y), args)

def read_preferences(file_name: str) -> dict:
    preferences = Group()
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.replace(",NA","")
            group_split = line.split(";")
            member_split = group_split[1].split(",")
            preferences.add_member(Member(group_split[0],member_split))
    return preferences

def stable_matching(proposers: Group, accepters: Group) -> None:
    unmatched_proposers = proposers.get_member_names()
    while len(unmatched_proposers) > 0:
        current_proposer = unmatched_proposers.pop()
        proposer_preferences = proposers.get_member_preferences(current_proposer)
        if proposer_preferences == []:
            proposers.set_member_match(current_proposer,"NO-MATCH")
            continue
        else:
            current_accepter = proposer_preferences[0]
        proposers.set_member_preferences(current_proposer,proposer_preferences[1:])
        if accepters.get_member_match(current_accepter) == None:
            proposers.set_member_match(current_proposer,current_accepter)
            accepters.set_member_match(current_accepter,current_proposer)
        else:
            accepter_preferences = accepters.get_member_preferences(current_accepter)
            previous_proposer = accepters.get_member_match(current_accepter)
            if current_proposer in accepter_preferences:
                current_proposer_index = accepter_preferences.index(current_proposer)
                if previous_proposer in accepter_preferences:
                    previous_proposer_index = accepter_preferences.index(previous_proposer)
                else:
                    previous_proposer_index = len(proposers.members)
                if current_proposer_index < previous_proposer_index:
                    unmatched_proposers = [previous_proposer] + unmatched_proposers
                    proposers.set_member_match(current_proposer,current_accepter)
                    accepters.set_member_match(current_accepter,current_proposer)
                else:
                    unmatched_proposers = [current_proposer] + unmatched_proposers
            else:
                unmatched_proposers = [current_proposer] + unmatched_proposers

def get_remaining_unmatched_proposers(proposers: Group) -> Group:
    remaining_proposers = Group()
    for key,value in proposers.members.items():
        if value.match == None or value.match == "NO-MATCH":
            remaining_proposers.add_member(value)
    return remaining_proposers

def get_pairings_as_str(proposers: Group, proposer_group_name: str, accepter_group_name: str) -> str:
    pairings_string = ""
    for proposer in sorted(proposers.get_member_names()):
        pairings_string += "{} = {}; {} = {}".format(proposer_group_name,proposer,accepter_group_name,proposers.get_member_match(proposer)) + "\n"
    return pairings_string

def run_stable_matching(proposer_file_name: str, accepter_file_name: str, proposer_group_name: str, accepter_group_name: str) -> None:
    proposers = read_preferences(proposer_file_name)
    accepters = read_preferences(accepter_file_name)
    stable_matching(proposers,accepters)
    print(get_pairings_as_str(proposers,proposer_group_name,accepter_group_name))
    print("----------")
    print()

if __name__ == "__main__":
    run_stable_matching(join_path("data","men1.txt"),join_path("data","women1.txt"),"Husband","Wife")
    run_stable_matching(join_path("data","men2.txt"),join_path("data","women1.txt"),"Husband","Wife")
    run_stable_matching(join_path("data","men3.txt"),join_path("data","women1.txt"),"Husband","Wife")
    run_stable_matching(join_path("data","men4.txt"),join_path("data","women1.txt"),"Husband","Wife")
    run_stable_matching(join_path("data","m.txt"),join_path("data","w.txt"),"Husband","Wife")
