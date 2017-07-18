from views import ui
from views import mentor_view
from views import student_view


def print_manager_menu():
    title = 'Manager Menu'
    options = ['List mentors',
               'View mentor details',
               'Add mentor',
               'Remove mentor',
               'Edit mentor',
               'List students',
               'View students details'
               ]

    ui.print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3', '4', '5', '6', '7']
    choice = ''
    while choice not in possible_choices:
        choice = ui.get_inputs(['option:'], 'Choose option')[0]

    return choice


def list_users(users_list):
    print(' ' + '=' * 62)
    print('|{:<20}|{:<20}|{:<20}|'.format('id', 'name', 'surname'))
    print('|{:<20}|{:<20}|{:<20}|'.format('', '', '').replace(' ', '+'))
    for user in users_list:
        print('|{:<20}|{:<20}|{:<20}|'.format(str(user.id_), user.name, user.surname))

    print(' ' + '=' * 62)


def get_id():
    return ui.get_inputs(['id:'], 'Provide id')[0]


def print_mentor(mentor):
    mentor_view.print_mentor_details(mentor)


# def get_new_mentor_data():
#     mentor_attributes_names = ['name', 'surname', 'login', 'password', 'email', 'phone']
#     data = ui.get_inputs(mentor_attributes_names, 'Provide data for mentor')

#     return data


def list_all_students(students_list):
    print(' ' + '=' * 41)
    print('|{:<20}|{:<20}|'.format('id', 'name'))
    print('|{:<20}|{:<20}|'.format('', '').replace(' ', '+'))
    for student in students_list:
        print('|{:<20}|{:<20}|'.format(str(student.id_), student.name))

    print(' ' + '=' * 41)


def print_student(student):
    student_view.print_student_details(student)
