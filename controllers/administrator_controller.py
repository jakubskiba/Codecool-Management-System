import os

from views import administrator_view
from views import user_view


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
        os.system('clear')
        user_view.display_user_info(administrator)
        administrator_view.print_administrator_menu()
        choice = administrator_view.get_choice()

        if choice == '1':
            administrator_view.print_students_list(school)

        input('Press enter')
