from views.manager_view import *
from models.mentor_model import Mentor
from models.user_model import User


def start_controller(school, manager):
    choice = ''
    while choice != '0':
        print_manager_menu()
        choice = get_choice()

        if choice == '1':
            list_users(school.mentors_list)

        elif choice == '2':
            view_mentor_details(school)

        elif choice == '3':
            add_mentor(school)

        elif choice == '4':
            remove_mentor(school)

        elif choice == '5':
            list_all_students(school.students_list)

        elif choice == '6':
            view_student_details(school)


def get_user(school, users_list):
    possible_ids = [str(user.id_) for user in users_list]
    chosen_user_id = ''
    while chosen_user_id not in possible_ids:
        list_users(users_list)
        chosen_user_id = get_id()
    chosen_user_id = int(chosen_user_id)

    for user in users_list:
        if chosen_user_id == user.id_:
            chosen_user = user

    return chosen_user


def get_mentor(school):
    return get_user(school, school.mentors_list)


def get_student(school):
    return get_user(school, school.students_list)


def view_mentor_details(school):
    chosen_mentor = get_mentor(school)
    print_mentor(chosen_mentor)


def add_mentor(school):
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


def remove_mentor(school):
    mentor_to_remove = get_mentor(school)
    school.mentors_list.remove(mentor_to_remove)


def view_student_details(school):
    chosen_student = get_student(school)
    print_student(chosen_student)
