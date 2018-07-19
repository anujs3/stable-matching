from stable_matching import *
import random

def get_random_preferences(pickers: [str], people_to_choose_from: [str]) -> [[str]]:
    result = []
    for i in range(len(pickers)):
        preferences = []
        number_selected = 0
        while number_selected < 3:
            random_person = people_to_choose_from[random.randrange(len(people_to_choose_from))]
            if random_person not in preferences:
                preferences.append(random_person)
                number_selected += 1
        result.append(preferences)
    return result

def open_file_and_get_lines(file_path: str) -> [str]:
    with open(file_path, "r") as file:
        return get_stripped_lines(file)

def get_stripped_lines(file) -> [str]:
    return [line.strip().strip(";") for line in file.readlines()]

def write_populated_file(file_path: str, pickers: [str], preferences: [[str]]):
    with open(file_path, "w") as file:
        for picker_number in range(len(pickers)):
            file.write(pickers[picker_number] + ";" + ",".join(preferences[picker_number]) + "\n")

def main():
    mentee_file_path = join_path("data","fake_mentee_list.txt")
    mentor_file_path = join_path("data","full_mentor_list.txt")

    new_mentee_file_path = join_path("data","populated_mentee_list.txt")
    new_mentor_file_path = join_path("data","populated_mentor_list.txt")

    mentee_lines = open_file_and_get_lines(mentee_file_path)
    mentor_lines = open_file_and_get_lines(mentor_file_path)

    random_mentee_preferences = get_random_preferences(mentee_lines, mentor_lines)
    random_mentor_preferences = get_random_preferences(mentor_lines, mentee_lines)

    write_populated_file(new_mentee_file_path, mentee_lines, random_mentee_preferences)
    write_populated_file(new_mentor_file_path, mentor_lines, random_mentor_preferences)

if __name__ == "__main__":
    main()
