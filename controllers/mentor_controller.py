from models.mentor_model import Mentor
from models.user_model import User
from views.mentor_view import *


def start_controller(codecool, mentor):
    choice = ''
    while choice != '0':
        print_mentor_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(codecool)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass


def submit_assignment():
    pass
