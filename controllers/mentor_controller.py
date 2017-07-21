import os
# Mentor : jest szansa że to jest niepotrzebne, ale mózg mi paruje i na wszelkie wypadek nie usunem
from models import mentor_model
from models import user_model  # User : to tesz
from models import student_model  # Student : i to

from views import mentor_view
from views import assignment_view
from views import assignment_submission_view
from views import ui
from views import user_view
from views import manager_view

from models import assignment_model
from models import attendance_model
from datetime import datetime

from controllers import user_controller
from controllers import school_controller
from controllers import mail_controller

import utilities


def get_attendance_object(student, date):
    """
    Returns object of Attendance class belonging to given user and having given date

    Args:
        student (Student): object of Student class
        date (datetime): datetime object

    Returns:
        attendance (Attendance): object of Attendabce class belonging to given user and having given date

    """

    for attendance in student.attendance_list:
        if attendance.date.date() == date.date():
            return attendance


def check_today_attendance(codecool):
    """
    Checks today attendance of the whole class

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    today = datetime.now()
    if get_attendance_object(codecool.students_list[0], today):
        ui.print_error_message('Today attendance is already checked')
    else:
        ui.print_message('''Checking attendance for today.
        0 - absent
        0.5 - late
        1 - present''')
        for student in codecool.students_list:
            attendance_state = ''
            while attendance_state not in ['0', '0.5', '1']:
                attendance_state = ui.get_input(student.name + ' ' + student.surname)
            attendance_state = float(attendance_state)
            student.attendance_list.append(attendance_model.Attendance(today, attendance_state, student))


def change_chosen_attendance(codecool):
    """
    Change status of chosen attendence object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """
    try:
        chosen_student = get_student(codecool)
        mentor_view.print_student_attendances(chosen_student)
        try:
            attendance_id_ = ui.get_input('Choose attendance id')
            ui.print_message(
                'current state is: ' + str(chosen_student.attendance_list[int(attendance_id_)].attendance_state))
            ui.print_message('''Possible attendance grades:
            0 - absent
            0.5 - late
            1 - present''')
            attendance_state = ''
            while attendance_state not in ['0', '0.5', '1']:
                attendance_state = ui.get_input('Choose new attendance grade')
            chosen_student.attendance_list[int(attendance_id_)].attendance_state = float(attendance_state)
        except (IndexError, ValueError) as er:
            ui.print_error_message('There is no such attendance')
    except AttributeError:
        pass


def add_new_assignment(codecool):
    """
    Append assignments_list by new created assignment object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        None
    """

    assignment_view.print_add_assignment_title()
    content = assignment_view.get_assignment_content()
    year = assignment_view.get_assignment_year()
    month = assignment_view.get_assignment_month()
    day = assignment_view.get_assignment_day()
    try:
        date = datetime(int(year), int(month), int(day))
        assignment = assignment_model.Assignment(content, date, assignment_model.Assignment.last_id + 1)
        codecool.assignments_list.append(assignment)
        assignment_view.print_assignment_details(assignment)
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

    mentor_view.print_students_list(codecool)
    student_id = ui.get_inputs([''], 'Choose student id')

    try:
        student = choose_student_by_id(int(student_id[0]), codecool)
        id_ = 1
        for subm in student.assignment_submissions:
            assignment_submission_view.print_submission(id_, subm)
            id_ += 1
        id_ = ui.get_inputs(['id'], 'Provide submission id:')[0]

        try:
            submission_to_mark = choose_submission_by_id(id_, student)
        except ValueError:
            ui.print_error_message('No such submission')

        try:
            submission_to_mark.grade = int(ui.get_inputs(['mark'], 'Provide mark')[0])
        except ValueError:
            ui.print_error_message('Grade must be integer number')

    except ValueError:
        ui.print_error_message('There is no such student')


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
    user_controller.add_user(codecool, 'student')


def get_student(codecool):
    """
    Returns student object

    Args:
        codecool (obj): School object - aggregate all users and assignments

    Returns:
        Student (obj)
    """

    return school_controller.get_user(codecool, codecool.students_list)


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
    user_controller.start_controller(student_to_change)


def print_student_details(codecool):
    """
    Ask for student id, then print student details

    Args:
        codecool (obj): school object - aggregate all users and assignments

    Returns:
        None
    """

    chosen_student = get_student(codecool)
    if chosen_student:
        manager_view.print_student(chosen_student)


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
        user_view.display_user_info(mentor)
        mentor_view.print_mentor_menu()
        choice = mentor_view.get_choice()

        if choice == '1':
            mentor_view.print_students_list(codecool)
        elif choice == '2':
            print_student_details(codecool)
        elif choice == '3':
            add_new_assignment(codecool)
        elif choice == '4':
            grade_assignment(codecool)
        elif choice == '5':
            add_student(codecool)
        elif choice == '6':
            remove_student(codecool)
        elif choice == '7':
            edit_student(codecool)
        elif choice == '8':
            check_today_attendance(codecool)
        elif choice == '9':
            change_chosen_attendance(codecool)
        elif choice == '10':
            mail_controller.start_controller(codecool, mentor)

        input('Press enter')
