from views import ui
from views import assignment_view
from views import attendance_view


def print_mentor_details(mentor):
    """
    Function prints mentor details

    Args:
        mentor (Mentor): object represents single mentor

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Mentor id:', mentor.id_)
    print('Full name:', mentor.name, mentor.surname)
    print('E-mail:', mentor.email)
    print('Phone:', mentor.phone)
    print(ornament)


def print_students_list(codecool):
    title_list = ['id', 'Name', 'Surname']

    table = []
    for student in codecool.students_list:
        table.append([student.id_, student.name, student.surname])

    ui.print_table(table, title_list)


def print_mentor_menu():
    title = 'Mentor Menu'
    options = ['List students', 'Show student details', 'Add assignments', 'Grade assignment', 'Add student',
               'Remove student', 'Edit student', 'Check today attendance', 'Change chosen attendance state', 'Mail']

    ui.print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    choice = ''
    while choice not in possible_choices:
        choice = ui.get_inputs(['option:'], 'Choose option')[0]

    return choice


def print_all_assignments(codecool):
    for assignment in codecool.assignments_list:
        assignment_view.print_assignment_details(assignment)
        print()


def get_id():
    return ui.get_inputs(['id:'], 'Provide id')[0]


def get_input(msg):
    a = input(msg)
    return a


def print_student_attendances(student):
    table = []
    id_ = 0
    for attendance in student.attendance_list:
        table.append([str(id_), str(attendance.date.date()), str(attendance.attendance_state)])
        id_ += 1
    headers = ['id', 'date', 'grade']
    ui.print_table(table, headers)
