from student_model import Student
from datetime import datetime


class Attendance():
    """
    Attendance class is model of attendance

    Attributes:
        date (datetime): date and hour when attendence was checked
        attendance_state (float): attendence factor
            0 means student was on absent
            0.5 means student was late
            1 means student was on time
        student (obj): points on Student objct who was checked
    """

    def __init__(self, date, attendance_state, student):
        """
        Raises:
            TypeError: when date is not datetime type
            ValueError: when attendance_state is not convertable to float
            TypeError: when student is not Student object
        """
        if not isinstance(date, datetime):
            raise TypeError(str(date) + ' is not datetime type')
        else:
            self.date = date

        self.attendance_state = float(attendance_state)

        if not isinstance(student, Student):
            raise TypeError(student + ' is not Student object')
        else:
            self.student = student
