from views.ui import print_menu
from views.ui import get_inputs
from views.assignment_submission_view import print_submission
from views.assignment_view import print_assignment_details


def print_student_menu():
    title = 'Student Menu'
    options = ['Submit assignment', 'View available assignments', 'View my grades']

    print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3']
    choice = ''
    while choice not in possible_choices:
        choice = get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_all_submissions(assignment_submissions):
    for submission in assignment_submissions:
        print_submission(submission)
        print()


def print_all_assignments(assignments_list):
    for assignment in assignments_list:
        print_assignment_details(assignment)
        print()


def get_assignment_id():
    return get_inputs(['assignment id:'], 'Provide assignment id')[0]
