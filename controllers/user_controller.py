from models.user_model import User
from views.user_view import *


def main():
    wera = User('w', 'd', 'wd', 'p', '@', '123', 0)
    display_update_choice(wera)
    a = get_input()