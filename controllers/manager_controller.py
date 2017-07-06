from views.manager_view import *


def start_controller(School, manager):
    choice = ''
    while choice != '0':
        print_manager_menu()
        choice = get_choice()

        if choice == '1':
            list_all_mentors(School.mentors_list)
            pass
        elif choice == '2':
            # View mentor details
            pass
        elif choice == '3':
            # Add mentor
            pass
        elif choice == '4':
            # Remove mentor
            pass
        elif choice == '5':
            # List students
            pass
        elif choice == '6':
            # View students details
            pass
