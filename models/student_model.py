from models.user_model import User


class Student(User):
    """
    Attributes:
        assignment_submisions (list)
        grades_submissions (list)
        attendance_list (list)
    """

    def __init__(self, assignment_submissions, grades_submissions, attendance_list):
        if isinstance(assignment_submissions, list):
            self.assignment_submissions = assignment_submissions
        else:
            raise TypeError(assignment_submissions + ' is not list')

        if isinstance(grades_submissions, list):
            self.grades_submissions = grades_submissions
        else:
            raise TypeError(grades_submissions, + ' is not list')

        if isinstance(attendance_list):
            self.attendance_list = attendance_list
        else:
            raise TypeError(attendance_list + ' is not list')
