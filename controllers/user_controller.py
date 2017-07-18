from models import user_model
from views import user_view
import utilities


def start_controller(user):
    """
    Calls updater function

    Args:
        user (obj): User object

    Returns:
        None
    """

    display_update_choice(user)
    which_data = get_data_number()
    updater(user, which_data)


def updater(user, which_data):
    """
    Updates data in user object

    Args:
        user (obj): User object
        which_data (str)
    """

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


def add_user(school, kind='student'):
    """
    Appends users_list in school object by new created user object
    Prints error message if login is not unique

    Args:
        school (obj): school object - aggregate all users and assignments
        kind (str): information lets add object to proper list

    Returns:
        None
    """

    user_data = views.user_view.get_new_user_data()

    name = user_data[0]
    surname = user_data[1]
    login = user_data[2]
    password = user_data[3]
    email = user_data[4]
    phone = user_data[5]

    id_ = user_model.User.last_id + 1

    password = utilities.hash_password(password)

    users = school.managers_list + school.administrators_list + school.mentors_list + school.students_list
    users_logins = [user.login for user in users]

    if kind == 'mentor':
        users_list = school.mentors_list
    else:
        users_list = school.students_list

    if login not in users_logins:
        new_user = user_model.User(name, surname, login, password, email, phone, id_)
        users_list.append(new_user)
    else:
        views.ui.print_error_message('login already in use')


def get_new_user_data():
    pass