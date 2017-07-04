from datetime import date
import views.assignment_view


class Assignment:
    def __init__(self, content, deadline, assignment_id):
        """
        Method creates an instance of the class

        Args:
            content (str): description of the assignment
            deadline (Date): object of Date class
            assignment_id (int): order number of the assignment

        Returns:
            None
        """

        if type(content) is str and type(deadline) is date and type(assignment_id) is int:
            self.content = content
            self.deadline = deadline
            self.assignment_id = assignment_id
        else:
            raise TypeError


def main():
    c = Assignment('pikuś', date(2017, 4, 12), 5)
    print(c)


if __name__ == '__main__':
    main()
