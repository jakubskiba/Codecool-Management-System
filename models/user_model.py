class User():
    
    def __init__(self, name, surname, login, password, email, phone, id_):
        '''
        sets User objects
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
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone
        self.id_ = id_
