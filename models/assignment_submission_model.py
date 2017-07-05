from models.student_model import Student
from models.assignment_model import Assignment
from datetime import date


class Assignment_Submission():

    def __init__(student, date_of_submission, content, assignment):

        '''
        initialize Assignment_submission object
        Args:
            student: Student instance object
            date: Datetime
            content: str
            assignment: Assignment object
            grade: int
        '''
        if type(student) == Student and type(date_of_submission) == date and 
           type(content) == str and type(assignment) == Assignment:
           
            self.student = student
            self.date_of_submission = date_of_submission
            self.content = content
            self.assignment = assignment

        else:
            raise TypeError

        self.grade = 0