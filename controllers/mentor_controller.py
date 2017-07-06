from models.mentor_model import Mentor
from models.user_model import User
from views.mentor_view import *
from views.assignment_view import *
from models.assignment_model import Assignment
from datetime import datetime
import views.ui
from views.assignment_submission_view import *
from models.student_model import Student


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


def add_student(codecool):
    student_data = get_new_student_data()

    name = student_data[0]
    surname = student_data[1]
    login = student_data[2]
    password = student_data[3]
    email = student_data[4]
    phone = student_data[5]

    id_ = User.last_id + 1

    new_student = Student(name, surname, login, password, email, phone, id_)

    codecool.students_list.append(new_student)


def remove_mentor(school):
    mentor_to_remove = get_mentor(school)
    school.mentors_list.remove(mentor_to_remove)


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
            add_student(codecool)
        elif choice == '5':
            pass
