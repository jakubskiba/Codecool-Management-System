from controllers import user_controller
from controllers import school_controller

from models import mentor_model
from models import user_model

from views import user_view
from views import manager_view
from views import ui

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
        user_view.display_user_info(manager)
        manager_view.print_manager_menu()
        choice = manager_view.get_choice()

        if choice == '1':
            manager_view.list_users(school.mentors_list)

        elif choice == '2':
            view_mentor_details(school)

        elif choice == '3':
            add_mentor(school)

        elif choice == '4':
            remove_mentor(school)

        elif choice == '5':
            edit_mentor(school)

        elif choice == '6':
            manager_view.list_all_students(school.students_list)

        elif choice == '7':
            view_student_details(school)

        input('Press enter')


def get_mentor(school):
    """
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        Mentor object
    """

    return school_controller.get_user(school, school.mentors_list)


def get_student(school):
    """
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        Student object
    """

    return school_controller.get_user(school, school.students_list)


def view_mentor_details(school):
    """
    Ask for mentor id, then print mentor details
    Args:
        school (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    chosen_mentor = get_mentor(school)
    if chosen_mentor:
        manager_view.print_mentor(chosen_mentor)


def add_mentor(school):

    user_controller.add_user(school, 'mentor')


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
    if chosen_student:
        manager_view.print_student(chosen_student)


def edit_mentor(school):
    """
    Changes mentor data

    Args:
        school (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    mentor_to_change = get_mentor(school)
    user_controller.start_controller(mentor_to_change)
