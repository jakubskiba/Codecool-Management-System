class User():
    
    def __init__(self, name, surname, login, password, email, phone, id_):
        '''
        Abstract class, sets User objects, to inherit by Mentor, Administrator, Student, Manager
        Args:
            name: str
            surname: str
            login: str
            password: str
            email: str
            phone: str
            id_: int
        Returns:
            None
        '''

        # to condition initializing instance with is_login_unique function 
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone
        self.id_ = id_
