def print_mentor_details(mentor):
    """
    Function prints mentor details

    Args:
        mentor (Mentor): object represents single mentor

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Mentor id:', mentor.id)
    print('Full name:', mentor.name, mentor.surname)
    print('E-mail:', mentor.e_mail)
    print('Phone:', mentor.phone)
    print(ornament)
