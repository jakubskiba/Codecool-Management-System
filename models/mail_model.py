from datetime import datetime


class Mail():
    def __init__(self, date, sender, receiver, topic, message):
        self.sender = sender
        self.receiver = receiver
        self.topic = topic
        self.message = message
        self.date = date
        self.state = 'unread'
