import os

from models.school_model import School
from models.user_model import User
from models.manager_model import Manager
from models.administrator_model import Administrator
from models.mentor_model import Mentor
from models.student_model import Student

from models.assignment_model import Assignment
from models.assignment_submission_model import AssignmentSubmission
from models.attendance_model import Attendance

from views import school_view
from views import manager_view
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
        codecool = School()
        database.load_files(codecool)

        user = log_in(codecool)
        if type(user) is Manager:
            manager_controller.start_controller(codecool, user)
        elif type(user) is Administrator:
            administrator_controller.start_controller(codecool, user)
        elif type(user) is Mentor:
            mentor_controller.start_controller(codecool, user)
        elif type(user) is Student:
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
        views.ui.print_error_message('No such user')
