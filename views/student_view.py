from views.ui import print_menu
from views.ui import get_inputs


def print_student_menu():
    title = 'Student Menu'
    options = ['Submit assignment', 'View my grades']

    print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2']
    choice = ''
    while choice not in possible_choices:
        choice = get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_all_submissions(student):
    submissions_representation = []
    for submission in student.assignment_submissions:
        submissions_representation.append(str(submission.asignment_id), submission.content[:10], str(submission.grade))
    print_menu('Submissions', submissions_representation, 'Return')


def get_submission_number():
    pass