from models import user_model


class Student(user_model.User):
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
    
    def get_attendance(self):
        """
        Computes attendance percent based on attendance list

        Return (float): percentage of attendance
        """

        if len(self.attendance_list):
            attendance_sum = 0
            for attendance in self.attendance_list:
                attendance_sum += attendance.attendance_state
            return attendance_sum/len(self.attendance_list) * 100

        else:
            return 100.0 
