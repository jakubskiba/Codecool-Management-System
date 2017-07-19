import os

from views import administrator_view
from views import mail_view
from views import user_view

from controllers import mail_controller


def start_controller(school, administrator):
    """
    Switches between options

    Args:
        school (obj): school object - aggregate all users and assignments
        administrator (obj): Administrators object

    Returns:
        None
    """

    print(school.mails[0].receiver.name)

    choice = ''
    while choice != '0':
        os.system('clear')
        user_view.display_user_info(administrator)
        administrator_view.print_administrator_menu()
        choice = administrator_view.get_choice()

        if choice == '1':
            administrator_view.print_students_list(school)

        if choice == '2':
            mail_controller.start_controller(school, administrator)

        input('Press enter')
