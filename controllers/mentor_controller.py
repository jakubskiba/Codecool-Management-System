from models.mentor_model import Mentor
from models.user_model import User
from views.mentor_view import *
from views.assignment_view import *
from models.assignment_model import Assignment
from datetime import datetime
import views.ui
from views.assignment_submission_view import *


def add_new_assignment(codecool):
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
    for student in codecool.students_list:
        if student.id_ == id_:
            return student
    raise ValueError


def grade_assignment(codecool):
    print_students_list(codecool)
    student_id = views.ui.get_inputs([''], 'Choose student id')

    try:
        student = choose_student_by_id(int(student_id[0]), codecool)
        for subm in student.assignment_submissions:
            print_submission(subm)

        id_ = input('Which assignment to grade?')

        try:
            submission_to_mark = choose_submission_by_id(id_, student)

            submission_to_mark.grade = int(input('What is your mark?'))

        except ValueError:
            views.ui.print_error_message('There is no such submission')

    except ValueError:
        views.ui.print_error_message('There is no such student')


def choose_submission_by_id(id_, student):
    for subm in student.assignment_submissions:
        if subm.id_ == id_:
            return subm
    return ValueError


def start_controller(codecool, mentor):
    choice = ''
    while choice != '0':
        print_mentor_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(codecool)
        elif choice == '2':
            add_new_assignment(codecool)
        elif choice == '3':
            grade_assignment(codecool)
        elif choice == '4':
            pass
        elif choice == '5':
            pass


def submit_assignment():
    pass
