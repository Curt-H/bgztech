# Create your models here.
from mongoengine import *

connect('bgztech')


class Dict(Document):
    word = StringField(required=True, unique=True)
    paraphrase = ListField(DictField)
