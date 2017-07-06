from views.student_view import *
from models.assignment_submission_model import AssignmentSubmission
from datetime import datetime


def start_controller(school, student):
    choice = ''
    while choice != '0':
        print_student_menu()
        choice = get_choice()

        if choice == '1':
            submit_assignment(school, student)
        elif choice == '2':
            list_assignments(school)
        elif choice == '3':
            get_assignment_submissions(student)


def get_assignment_submissions(student):
    print_all_submissions(student.assignment_submissions)


def list_assignments(school):
    print_all_assignments(school.assignments_list)


def get_assignment_submissions(student):
    pass
