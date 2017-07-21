from models import user_model
from models import student_model
from models import mentor_model
from views import user_view
from views import ui
import utilities
import re


def start_controller(user):
    """
    Calls updater function

    Args:
        user (obj): User object

    Returns:
        None
    """

    user_view.display_update_choice(user)
    which_data = user_view.get_data_number()
    updater(user, which_data)


def updater(user, which_data):
    """
    Updates data in user object

    Args:
        user (obj): User object
        which_data (str)
    """

    if which_data == '1':
        user_view.display_old_data(user.email)
        user.email = update_data('email', is_email, user.email)
    elif which_data == '2':
        user_view.display_old_data(user.name)
        user.name = update_data('name', is_name_alpha, user.name)
    elif which_data == '3':
        user_view.display_old_data(user.password)
        user.password = update_data('password', is_password_sufficient, user.password)
    elif which_data == '4':
        user_view.display_old_data(user.phone)
        user.phone = update_data('phone', is_phone_number, user.phone)
    elif which_data == '5':
        user_view.display_old_data(user.surname)
        user.surname = update_data('surname', is_name_alpha, user.surname)


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

    try:
        name = create_data_for_user('name', is_name_alpha)
        surname = create_data_for_user('surname', is_name_alpha)
        login = create_login(school)
        password = create_data_for_user('password', is_password_sufficient)
        email = create_data_for_user('email', is_email)
        phone = create_data_for_user('phone', is_phone_number)

        id_ = user_model.User.last_id + 1

        password = utilities.hash_password(password)

        if kind == 'mentor':
            users_list = school.mentors_list
        else:
            users_list = school.students_list

        if kind == 'student':
            new_user = student_model.Student(name, surname, login, password, email, phone, id_)
        else:
            new_user = mentor_model.Mentor(name, surname, login, password, email, phone, id_)
        users_list.append(new_user)

    except ValueError:
        ui.print_error_message('Adding user was interrupted')


def create_data_for_user(data_type, condition):

        new_data = user_view.get_new_user_data(data_type)[0]

        while not condition(new_data):
            if user_view.get_yn_answer('Do you want to keep adding user [y/n]?') == 'y':
                new_data = user_view.get_new_user_data(data_type)[0]
            else:
                raise ValueError

        return new_data


def create_login(school):

    new_login = user_view.get_new_user_data('login')[0]

    while not is_login_available(new_login, school):
        if user_view.get_yn_answer('Do you want to keep adding user [y/n]?') == 'y':
                new_login = user_view.get_new_user_data('login')[0]
        else:
            raise ValueError

    return new_login


def update_data(data_type, condition, old_data):

        new_data = user_view.get_new_user_data(data_type)[0]

        while not condition(new_data):
            if user_view.get_yn_answer('Do you want to keep update?') == 'y':
                new_data = user_view.get_new_user_data(data_type)[0]
            else:
                return old_data

        return new_data

            #  conditions

def is_login_available(login, school):

    users = school.managers_list + school.administrators_list + school.mentors_list + school.students_list
    users_logins = [user.login for user in users]
    if login and login not in users_logins:
        return True
    else:
        ui.print_error_message('login already in use')
        return False


def is_name_alpha(name):

    if name.isalpha():
        return True
    else:
        ui.print_error_message('Name musn\'t contain numbers nor be empty')
        return False


def is_password_sufficient(password):

    if len(password) < 8:
        ui.print_error_message('password must be at least 8 characters long')
        return False

    return True


def is_email(email):

    if re.match(r'(.+)@(.+)\.(.{2,})', email):
        return True
    else:
        ui.print_error_message('wrong email')
        return False


def is_phone_number(phone):

    if re.match(r'\d{9}', phone):
        return True
    else:
        ui.print_error_message('phone number is 9 digit number')
        return False
