from mongoengine import *


# Create your models here.

class Todo(Document):
    title = StringField(required=True)
    content = StringField()
    tag = ListField(StringField)
    creat_time = IntField(required=True)
    expired_time = IntField()
    repeat = BooleanField()
    repeat_mark = ListField(IntField)
