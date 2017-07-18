import os

from models import school_model
from models import user_model  # User : wygląda jakby tu nie było potrzebne
from models import manager_model
from models import administrator_model
from models import mentor_model
from models import student_model

from models import assignment_model  # Assignment : j. w.
from models import assignment_submission_model  # AssignmentSubmission : same story
from models import attendance_model  # Attendance : -||-

from views import school_view
from views import manager_view
from views import ui

from controllers import manager_controller
from controllers import administrator_controller
from controllers import mentor_controller
from controllers import student_controller
from controllers import database

import utilities


def log_in(codecool):
    """
    Checks is login and password belong to one same user

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        User (obj)
    """

    login = school_view.get_login()
    password = school_view.get_password()

    password = utilities.hash_password(password)

    users = codecool.managers_list + codecool.administrators_list + codecool.mentors_list + codecool.students_list
    for user in users:
        if user.login == login and user.password == password:
            return user


def start_controller():
    """
    Signs in user, then calls appropriate controller

    Returns:
        None
    """

    is_controller_running = True

    while is_controller_running:
        os.system('clear')
        school_view.intro()
        codecool = school_model.School()
        database.load_files(codecool)

        user = log_in(codecool)
        if type(user) is manager_model.Manager:
            manager_controller.start_controller(codecool, user)
        elif type(user) is administrator_model.Administrator:
            administrator_controller.start_controller(codecool, user)
        elif type(user) is mentor_model.Mentor:
            mentor_controller.start_controller(codecool, user)
        elif type(user) is student_model.Student:
            student_controller.start_controller(codecool, user)
        else:
            school_view.print_no_user_message()

        database.save_files(codecool)
        school_view.print_exit_message()

        if school_view.get_exit_decision():
            is_controller_running = False


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
    manager_view.list_users(users_list)
    chosen_user_id = manager_view.get_id()

    if chosen_user_id in possible_ids:
        chosen_user_id = int(chosen_user_id)

        for user in users_list:
            if chosen_user_id == user.id_:
                chosen_user = user

        return chosen_user
    else:
        ui.print_error_message('No such user')
