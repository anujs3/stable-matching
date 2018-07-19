from stable_matching import *
import populate_data_files

def test_stable_matching_with_men_and_women_simple_case():
    men = read_preferences(join_path("data","m.txt"))
    women = read_preferences(join_path("data","w.txt"))
    stable_matching(men,women)
    pairings = get_pairings_as_str(men,"Husband","Wife")
    assert pairings.strip() == open(join_path("test_data","marriage_simple_test.txt")).read().strip()

def test_stable_matching_with_men_and_women_case_1():
    men = read_preferences(join_path("data","men1.txt"))
    women = read_preferences(join_path("data","women1.txt"))
    stable_matching(men,women)
    pairings = get_pairings_as_str(men,"Husband","Wife")
    assert pairings.strip() == open(join_path("test_data","marriage_test1.txt")).read().strip()

def test_stable_matching_with_men_and_women_case_2():
    men = read_preferences(join_path("data","men4.txt"))
    women = read_preferences(join_path("data","women1.txt"))
    stable_matching(men,women)
    pairings = get_pairings_as_str(men,"Husband","Wife")
    assert pairings.strip() == open(join_path("test_data","marriage_test2.txt")).read().strip()

def test_stable_matching_with_mentees_and_mentors():
    mentees = read_preferences(join_path("data","mentees1.txt"))
    mentors = read_preferences(join_path("data","mentors1.txt"))
    stable_matching(mentees,mentors)
    pairings = get_pairings_as_str(mentees,"Mentee","Mentor")
    assert pairings.strip() == open(join_path("test_data","mentorship_test1.txt")).read().strip()

def test_remaining_mentees_with_no_match():
    mentees = read_preferences(join_path("data","mentees1.txt"))
    mentors = read_preferences(join_path("data","mentors1.txt"))
    stable_matching(mentees,mentors)
    remaining_mentees = get_remaining_unmatched_proposers(mentees)
    assert sorted(remaining_mentees.get_member_names()) == ["D","E","H","I","J"]

def test_if_mentee_or_mentor_does_not_have_a_top_three():
    mentees = read_preferences(join_path("data","mentees2.txt"))
    mentors = read_preferences(join_path("data","mentors2.txt"))
    stable_matching(mentees,mentors)
    pairings = get_pairings_as_str(mentees,"Mentee","Mentor")
    assert pairings.strip() == open(join_path("test_data","mentorship_test2.txt")).read().strip()

def test_with_random_data():
    populate_data_files.main()
    mentees = read_preferences(join_path("data","populated_mentee_list.txt"))
    mentors = read_preferences(join_path("data","populated_mentor_list.txt"))
    stable_matching(mentees,mentors)
    print(get_pairings_as_str(mentors,"Mentor","Mentee"))
    print()
    print(get_pairings_as_str(mentees,"Mentee","Mentor"))
