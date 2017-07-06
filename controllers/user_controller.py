from models.user_model import User
from views.user_view import *


def start_controller(user):
    display_update_choice(user)
    which_data = get_data_number()
    updater(user, which_data)


def updater(user, which_data):

    data_dict = {1: 'email', 2: 'login', 3: 'name', 4: 'password', 5: 'phone', 6: 'surname'}

    if which_data == '1':
        user.email = get_updated_string(data_dict[1])
    elif which_data == '2':
        user.login = get_updated_string(data_dict[2])
    elif which_data == '3':
        user.name = get_updated_string(data_dict[3])
    elif which_data == '4':
        user.password = get_updated_string(data_dict[4])
    elif which_data == '5':
        user.phone = get_updated_string(data_dict[5])
    elif which_data == '6':
        user.surname = get_updated_string(data_dict[6])
