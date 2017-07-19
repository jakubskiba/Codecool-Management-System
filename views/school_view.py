from views import ui
import getpass


def intro():
    print('Welcome to New Canvas!')
    print('Log in to start!')


def get_login():
    return input('Input your login: ')


def get_password():
    return getpass.getpass('Input your password: ')


def print_exit_message():
    print('Thank you for using New Canvas! See you next time.')


def print_no_user_message():
    print('There is no such user in system!')


def get_exit_decision():
    decision = input('Do you want to exit program (Y/n)? ').lower()
    if decision == 'n':
        return False
    else:
        return True


def print_mentors_list(codecool):
    title_list = ['id', 'Name', 'Surname']

    table = []
    for mentor in codecool.mentors_list:
        table.append([mentor.id, mentor.name, mentor.surname])

    ui.print_table(table, title_list)
