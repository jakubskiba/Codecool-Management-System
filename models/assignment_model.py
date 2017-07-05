from datetime import datetime


class Assignment:
    def __init__(self, content, deadline, assignment_id):
        """
        Method creates an instance of the class

        Args:
            content (str): description of the assignment
            deadline (Datetime): object of Datetime class
            assignment_id (int): order number of the assignment

        Returns:
            None
        """

        if type(content) is str and type(deadline) is datetime and type(assignment_id) is int:
            self.content = content
            self.deadline = deadline
            self.assignment_id = assignment_id
        else:
            raise TypeError


def main():
    c = Assignment('pikuś', datetime(2017, 4, 12), 5)
    print(type(c) == Assignment)


if __name__ == '__main__':
    main()
