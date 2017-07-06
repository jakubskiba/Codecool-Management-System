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
    for mentor in mentors_list:
        print_mentor_details(mentor)