from models.user_model import User


class Student(User):
    """
    Attributes:
        name (str)
        surname (str)
        login (str)
        password (str)
        email (str)
        phone (str)
        id_ (str)
        assignment_submissions (list)
        attendance_list (list)
    """

    def __init__(self, name, surname, login, password, email, phone, id_):
        super().__init__(name, surname, login, password, email, phone, id_)

        self.assignment_submissions = []
        self.attendance_list = []

