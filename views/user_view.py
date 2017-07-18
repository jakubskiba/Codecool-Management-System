from views import ui


def get_data_number():
    which_data = input()
    return which_data


def get_updated_string(data):
    '''
    Args:
        data: str (email/login/name/password/phone/surname)
    Return:
        updated_data: str
    '''
    question = 'What is your new {}?'.format(data)
    updated_data = input(question)

    return updated_data


def display_update_choice(user):

    attributes_list = [attr for attr in dir(user) if '_' not in attr]
    ui.print_menu('Which data to update? enter number', attributes_list, 'exit')


def display_user_info(user):
    """
    Displays who is logged in

    Args:
        user(obj)

    Returns:
        None
    """

    ornament = '=' * 30
    print(ornament)
    print('LOGGED USER')
    print(ornament)
    print('Name: {}\nSurname: {}\nPermissions: {}'.format(user.name, user.surname, user.__class__.__name__))
    print(ornament + '\n')


def get_new_user_data():

    user_attributes_names = ['name', 'surname', 'login', 'password', 'email', 'phone']
    data = ui.get_inputs(user_attributes_names, 'Provide data for user')

    return data
