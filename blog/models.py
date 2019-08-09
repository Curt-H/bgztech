from mongoengine import *

connect('bgztech')


# Create your models here.

class Users(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    role = StringField(default='user')


if __name__ == '__main__':
    class Test(Document):
        username = StringField(required=True)
        password = StringField(required=True)

    t = Test()
    t.username = 'test'
    t.password = 'test'
    t.save()
