import models.mentor_model
import models.user_model

import views.user_view
import views.manager_view
import views.ui

import utilities
import os


def start_controller(school, manager):
    """
    Switches between options

    Args:
        school (obj): school object - aggregate all users and assignments
        manager (obj): Manager object

    Returns:
        None
    """

    choice = ''
    while choice != '0':
        os.system('clear')
        views.user_view.display_user_info(manager)
        views.manager_view.print_manager_menu()
        choice = views.manager_view.get_choice()

        if choice == '1':
            views.manager_view.list_users(school.mentors_list)

        elif choice == '2':
            view_mentor_details(school)

        elif choice == '3':
            add_mentor(school)

        elif choice == '4':
            remove_mentor(school)

        elif choice == '5':
            views.manager_view.list_all_students(school.students_list)

        elif choice == '6':
            view_student_details(school)

        input('Press enter')


def get_user(school, users_list):
    """
    Ask user for id

    Args:
        school (obj): school object - aggregate all users and assignments
        user_list (list): in this list user will be searched

    Returns:
        User object
    """

    possible_ids = [str(user.id_) for user in users_list]
    chosen_user_id = ''
    while chosen_user_id not in possible_ids:
        views.manager_view.list_users(users_list)
        chosen_user_id = views.manager_view.get_id()
    chosen_user_id = int(chosen_user_id)

    for user in users_list:
        if chosen_user_id == user.id_:
            chosen_user = user

    return chosen_user


def get_mentor(school):
    """
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        Mentor object
    """

    return get_user(school, school.mentors_list)


def get_student(school):
    """
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        Student object
    """

    return get_user(school, school.students_list)


def view_mentor_details(school):
    """
    Ask for mentor id, then print mentor details
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    chosen_mentor = get_mentor(school)
    views.manager_view.print_mentor(chosen_mentor)


def add_mentor(school):
    """
    Appends mentors_list in school object by new created mentor object
    Prints error message if login is not unique

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    mentor_data = views.manager_view.get_new_mentor_data()

    name = mentor_data[0]
    surname = mentor_data[1]
    login = mentor_data[2]
    password = mentor_data[3]
    email = mentor_data[4]
    phone = mentor_data[5]

    id_ = models.user_model.User.last_id + 1

    password = utilities.hash_password(password)

    users = school.managers_list + school.administrators_list + school.mentors_list + school.students_list
    users_logins = [user.login for user in users]

    if login not in users_logins:
        new_mentor = models.mentor_model.Mentor(name, surname, login, password, email, phone, id_)
        school.mentors_list.append(new_mentor)
    else:
        views.ui.print_error_message('login already in use')


def remove_mentor(school):
    """
    Ask for mentor id then, deletes mentor from mentors_list in school object

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    mentor_to_remove = get_mentor(school)
    school.mentors_list.remove(mentor_to_remove)


def view_student_details(school):
    """
    Ask for mentor id, then print mentor details

    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    chosen_student = get_student(school)
    views.manager_view.print_student(chosen_student)
