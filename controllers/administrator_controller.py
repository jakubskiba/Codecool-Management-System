from models.administrator_model import Administrator
from models.school_model import School
from views.administrator_view import *


def start_controller(school, administrator):
    choice = ''
    while choice != '0':
        print_administrator_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(school)