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

    data_dict = {1: 'email', 2: 'login', 3: 'name', 4: 'password', 5: 'phone', 6: 'surname'}

    if which_data == '1':
        user.email = user_view.get_updated_string(data_dict[1])
    elif which_data == '2':
        user.login = user_view.get_updated_string(data_dict[2])
    elif which_data == '3':
        user.name = user_view.get_updated_string(data_dict[3])
    elif which_data == '4':
        user.password = user_view.get_updated_string(data_dict[4])
    elif which_data == '5':
        user.phone = user_view.get_updated_string(data_dict[5])
    elif which_data == '6':
        user.surname = user_view.get_updated_string(data_dict[6])


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
    
    name = user_view.get_new_user_data('name')[0]
    while not is_name_alpha(name):
        name = user_view.get_new_user_data('name')[0]

    surname = user_view.get_new_user_data('surname')[0]
    while not is_name_alpha(surname):
        surname = user_view.get_new_user_data('surname')[0]

    login = user_view.get_new_user_data('login')[0]
    while not is_login_available(login, school):
        login = user_view.get_new_user_data('login')[0]

    password = user_view.get_new_user_data('password')[0]
    while not is_password_sufficient(password):
        password = user_view.get_new_user_data('password')[0]

    email = user_view.get_new_user_data('email')[0]
    while not is_email(email):
        email = user_view.get_new_user_data('email')[0]

    phone = user_view.get_new_user_data('phone')[0]
    while not is_phone_number(phone):
        email = user_view.get_new_user_data('phone')[0]


    id_ = user_model.User.last_id + 1

    password = utilities.hash_password(password)

    if kind == 'mentor':
        users_list = school.mentors_list
    else:
        users_list = school.students_list

    if is_login_available(school, login):
        if kind == 'student':
            new_user = student_model.Student(name, surname, login, password, email, phone, id_)
        else:
            new_user = mentor_model.Mentor(name, surname, login, password, email, phone, id_)
        users_list.append(new_user)

    
def create_data_for_user(title, condition, school):

        new_data = user_view.get_new_user_data(title)[0]
        while not condition(title, school):
            if user_view.get_yn_answer('Do you want to keep adding user?') == 'y':
                new_data = user_view.get_new_user_data(title)[0]
            else:
                return None

        return new_data


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
