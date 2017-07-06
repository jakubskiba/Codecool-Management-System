from views.ui import print_menu
from views.ui import get_inputs
from views.mentor_view import print_mentor_details


def print_manager_menu():
    title = 'Manager Menu'
    options = ['List mentors',
               'View mentor details',
               'Add mentor',
               'Remove mentor',
               'List students',
               'View students details'
               ]

    print_menu(title, options, 'Exit')


def get_choice():
    possible_choices = ['0', '1', '2', '3', '4', '5', '6']
    choice = ''
    while choice not in possible_choices:
        choice = get_inputs(['option:'], 'Choose option')[0]

    return choice


def list_all_mentors(mentors_list):
    print(' ' + '=' * 41)
    print('|{:<20}|{:<20}|'.format('id', 'name'))
    print('|{:<20}|{:<20}|'.format('', '').replace(' ', '+'))
    for mentor in mentors_list:
        print('|{:<20}|{:<20}|'.format(str(mentor.id_), mentor.name))

    print(' ' + '=' * 41)


def get_mentor_id():
    return get_inputs(['mentor id:'], 'Provide mentor id')[0]


def print_mentor(mentor):
    print_mentor_details(mentor)


def get_new_mentor_data():
    mentor_attributes_names = ['name', 'surname', 'login', 'password', 'email', 'phone']
    data = get_inputs(mentor_attributes_names, 'Provide data for mentor')

    return data