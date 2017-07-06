from views.ui import print_menu


def get_input():
    which_data = input()
    return which_data


def display_update_choice(user):

    attributes_list = [attr for attr in dir(user) if '_' not in attr]
    print_menu('Which data to update? enter number', attributes_list, 'exit')