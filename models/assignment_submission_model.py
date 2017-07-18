from models import student_model
from models import assignment_model
from datetime import datetime


class AssignmentSubmission():

    def __init__(self, student, date_of_submission, content, assignment):

        '''
        initialize AssignmentSubmission object
        Args:
            student: Student instance object
            date: Datetime
            content: str
            assignment: Assignment object
            grade: int
        '''

        if type(student) == student_model.Student and type(date_of_submission) == datetime and type(content) == str and type(assignment) == assignment_model.Assignment:

            self.student = student
            self.date_of_submission = date_of_submission
            self.content = content
            self.assignment = assignment

        else:
            raise TypeError

        self.grade = 0
