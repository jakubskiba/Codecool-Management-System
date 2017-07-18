import os

from models.mentor_model import Mentor
from models.user_model import User
from models.student_model import Student

from views.mentor_view import *
from views.assignment_view import *
from views.assignment_submission_view import *
import views.ui

from models.assignment_model import Assignment
from datetime import datetime

from controllers.user_controller import add_user

import utilities


def add_new_assignment(codecool):
    """
    Append assignments_list by new created assignment object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None

    """

    print_add_assignment_title()
    content = get_assignment_content()
    year = get_assignment_year()
    month = get_assignment_month()
    day = get_assignment_day()
    try:
        date = datetime(int(year), int(month), int(day))
        assignment = Assignment(content, date, Assignment.last_id + 1)
        codecool.assignments_list.append(assignment)
        print_assignment_details(assignment)
    except (TypeError, ValueError) as er:
        print('Wrong values!')


def choose_student_by_id(id_, codecool):
    """
    Search for student with given id

    Args:
        id_ (int): student id
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        Student (obj)

    Raises:
        ValueError if student not found
    """

    for student in codecool.students_list:
        if student.id_ == id_:
            return student
    raise ValueError


def grade_assignment(codecool):
    """
    Changes grade attribute in assignment submission object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    print_students_list(codecool)
    student_id = views.ui.get_inputs([''], 'Choose student id')

    try:
        student = choose_student_by_id(int(student_id[0]), codecool)
        id_ = 1
        for subm in student.assignment_submissions:
            print('Submission id:', id_)
            print_submission(subm)
            id_ += 1
        id_ = input('Choose submission id: ')

        try:
            submission_to_mark = choose_submission_by_id(id_, student)

            submission_to_mark.grade = int(input('What is your mark?'))

        except ValueError:
            views.ui.print_error_message('There is no such submission')

    except ValueError:
        views.ui.print_error_message('There is no such student')


def choose_submission_by_id(id_, student):
    """
    Finds assignment submissions by id

    Args:
        id_ (int): given id
        student (obj): Student object

    Returns:
        AssignmentSubmissions (obj)

    Raises:
        ValueError if there is no such assignment submission in student object
    """

    if int(id_) in range(1, len(student.assignment_submissions) + 1):
        return student.assignment_submissions[int(id_)-1]
    else:
        raise ValueError


def add_student(codecool):
    add_user(codecool, 'student')
#     """
#     Append student to students_list in codecool object

#     Args:
#         codecool (obj): School object - aggregate all users and assignments

#     Returns:
#         None
#     """

#     student_data = get_new_student_data()

#     name = student_data[0]
#     surname = student_data[1]
#     login = student_data[2]
#     password = student_data[3]
#     email = student_data[4]
#     phone = student_data[5]

#     id_ = User.last_id + 1

#     password = utilities.hash_password(password)

#     new_student = Student(name, surname, login, password, email, phone, id_)

#     codecool.students_list.append(new_student)


def get_user(codecool, users_list):
    """
    Asks for user id

    Args:
        codecool (obj): School object - aggregate all users and assignments
        users_list (list): list of users

    Returns:
        User (obj)
    """

    possible_ids = [str(user.id_) for user in users_list]
    chosen_user_id = ''
    while chosen_user_id not in possible_ids:
        print_students_list(codecool)
        chosen_user_id = get_id()
    chosen_user_id = int(chosen_user_id)

    for user in users_list:
        if chosen_user_id == user.id_:
            chosen_user = user

    return chosen_user


def get_student(codecool):
    """
    Returns student object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        Student (obj)
    """

    return get_user(codecool, codecool.students_list)


def remove_student(codecool):
    """
    Deletes student from student list

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Return:
        None
    """

    student_to_remove = get_student(codecool)
    codecool.students_list.remove(student_to_remove)


def edit_student(codecool):
    """
    Changes student data

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Return:
        None
    """
    student_to_change = get_student(codecool)
    controllers.user_controller.start_controller(student_to_change)


def start_controller(codecool, mentor):
    """
    Switches between options

    Args:
        codecool (obj): School object - aggregate all users and assignments
        mentor (obj): Mentor object

    Returns:
        None
    """

    choice = ''
    while choice != '0':
        os.system('clear')
        views.user_view.display_user_info(mentor)
        print_mentor_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(codecool)
        elif choice == '2':
            add_new_assignment(codecool)
        elif choice == '3':
            grade_assignment(codecool)
        elif choice == '4':
            add_student(codecool)
        elif choice == '5':
            remove_student(codecool)
        elif choice == '6':
            edit_student(codecool)

        input('Press enter')
