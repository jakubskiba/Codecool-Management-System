from views.manager_view import *


def start_controller(school, manager):
    choice = ''
    while choice != '0':
        print_manager_menu()
        choice = get_choice()

        if choice == '1':
            list_all_mentors(School.mentors_list)
        elif choice == '2':
            view_mentor_details(school)
            pass
        elif choice == '3':
            # Add mentor
            pass
        elif choice == '4':
            # Remove mentor
            pass
        elif choice == '5':
            # List students
            pass
        elif choice == '6':
            # View students details
            pass


def view_mentor_details(school):
    mentors_ids = [str(mentor.id_) for mentor in school.mentors_list]

    chosen_mentor_id = ''
    while chosen_mentor_id not in mentors_ids:
        list_all_mentors(school.mentors_list)
        chosen_mentor_id = get_mentor_id()
    chosen_mentor_id = int(chosen_mentor_id)

    for mentor in school.mentors_list:
        if chosen_mentor_id == mentor.id_:
            chosen_mentor = mentor

    print_mentor(chosen_mentor)