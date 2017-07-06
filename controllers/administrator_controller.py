from models.administrator_model import Administrator
from models.school_model import School
from views.administrator_view import *


def start_controller(school, administrator):
    """
    Switches between options

    Args:
        school (obj): school object - aggregate all users and assignments
        administrator (obj): Administrators object

    Returns:
        None
    """

    choice = ''
    while choice != '0':
        print_administrator_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(school)