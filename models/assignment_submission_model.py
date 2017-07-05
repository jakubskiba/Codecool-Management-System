from models.student_model import Student
from models.assignment_model import Assignment
from datetime import date


class Assignment_Submission():

    def __init__(student, date, content, assignment):

        '''
        initialize Assignment_submission object
        Args:
            student: Student instance object
            date: Datetime
            content: str
            assignment: Assignment object
            grade: int
        '''

        self.student = student
        self.date = date
        self.content = content
        self.assignment = assignment
        
        self.grade = 0