from views import mail_view
from views import user_view
from controllers.database import get_user_by_id
from controllers import user_controller
from models import mail_model
import os
from datetime import datetime


def start_controller(codecool, user):
    choice = ''
    while choice != '0':
        os.system('clear')
        user_view.display_user_info(user)
        mail_view.print_mail_menu()
        choice = mail_view.get_choice()

        if choice == '1':
            show_incoming_mail(codecool, user)

        elif choice == '2':
            show_outcoming_mail(codecool, user)          

        elif choice == '3':
            write_email(codecool, user)

        if choice != '0':
            input('Press enter')


def show_incoming_mail(codecool, user):
    inbox = get_mails(codecool, user, 'in')
    mail_view.print_mail_list(inbox)

    idx = mail_view.get_mail_idx(inbox)

    if idx.isdigit() and int(idx) <= len(inbox):
        os.system('clear')
        idx = int(idx)
        mail = inbox[idx]
        mail_view.print_mail_verbosely(mail)


def show_outcoming_mail(codecool, user):
    outbox = get_mails(codecool, user, 'out')
    mail_view.print_mail_list(outbox)

    idx = mail_view.get_mail_idx(outbox)

    if idx.isdigit() and int(idx) <= len(outbox):
        os.system('clear')
        idx = int(idx)
        mail = outbox[idx]
        mail_view.print_mail_verbosely(mail)


def get_mails(codecool, user, category):
    mails = []
    for mail in codecool.mails:

        if category == 'in' and mail.receiver == user:
            mails.append(mail)
        elif category == 'out' and mail.sender == user:
            mails.append(mail)

    return mails


def write_email(codecool, user):
    pass