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
from views.school_view import *
import controllers.manager_controller
import controllers.administrator_controller
import controllers.mentor_controller
import controllers.student_controller
import controllers.database
import utilities


def log_in(codecool):
    """
    Checks is login and password belong to one same user

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        User (obj)
    """

    login = get_login()
    password = get_password()

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
        intro()
        codecool = School()
        controllers.database.load_files(codecool)

        user = log_in(codecool)
        if type(user) is Manager:
            controllers.manager_controller.start_controller(codecool, user)
        elif type(user) is Administrator:
            controllers.administrator_controller.start_controller(codecool, user)
        elif type(user) is Mentor:
            controllers.mentor_controller.start_controller(codecool, user)
        elif type(user) is Student:
            controllers.student_controller.start_controller(codecool, user)
        else:
            print_no_user_message()

        controllers.database.save_files(codecool)
        print_exit_message()

        if get_exit_decision():
            is_controller_running = False
