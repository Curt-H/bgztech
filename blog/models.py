from django import forms
from mongoengine import *

connect('bgztech')


# mongo DB models below
class Users(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(default='user')


if __name__ == '__main__':
    class Test(Document):
        username = StringField(required=True, unique=True)
        password = StringField(required=True)


    for i in range(2):
        t = Test()
        t.username = 'test'
        t.password = 'test'
        t.save()
