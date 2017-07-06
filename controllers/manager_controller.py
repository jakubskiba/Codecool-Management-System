from views.manager_view import *
from models.mentor_model import Mentor
from models.user_model import User


def start_controller(school, manager):
    choice = ''
    while choice != '0':
        print(User.last_id)
        print_manager_menu()
        choice = get_choice()

        if choice == '1':
            list_all_mentors(school.mentors_list)
        elif choice == '2':
            view_mentor_details(school)
            pass
        elif choice == '3':
            add_mentor(school, manager)

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


def add_mentor(school, manager):
    mentor_data = get_new_mentor_data()

    name = mentor_data[0]
    surname = mentor_data[1]
    login = mentor_data[2]
    password = mentor_data[3]
    email = mentor_data[4]
    phone = mentor_data[5]

    id_ = User.last_id + 1

    new_mentor = Mentor(name, surname, login, password, email, phone, id_)

    school.mentors_list.append(new_mentor)