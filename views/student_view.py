from views import ui
from views import assignment_submission_view
from views import assignment_view


def print_student_menu():
    title = 'Student Menu'
    options = ['Submit assignment', 'View available assignments', 'View my grades', 'Mail']

    ui.print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3', '4']
    choice = ''
    while choice not in possible_choices:
        choice = ui.get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_all_submissions(assignment_submissions):
    for submission in assignment_submissions:
        id_ = submission.assignment.assignment_id
        assignment_submission_view.print_submission(id_, submission)
        print()


def print_all_assignments(assignments_list):
    for assignment in assignments_list:
        assignment_view.print_assignment_details(assignment)
        print()


def get_assignment_id():
    return ui.get_inputs(['assignment id:'], 'Provide assignment id')[0]


def get_assignment_submission_content():
    return ui.get_inputs(['content:'], 'Provide content')[0]


def print_student_details(student):
    """
    Function prints mentor details

    Args:
        student (Student): object represents single student

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Mentor id:', student.id_)
    print('Full name:', student.name, student.surname)
    print('E-mail:', student.email)
    print('Phone:', student.phone)
    print('Attendance:', str(student.get_attendance()), '%')
    print(ornament)
