# Create your models here.
from mongoengine import *

connect('bgztech')


class Content(EmbeddedDocument):
    part_of_speech = StringField(required=True)
    paraphrase = StringField(required=True)
    example = StringField()


class Dict(Document):
    word = StringField(required=True, unique=True)
    contents = ListField(EmbeddedDocumentField(Content))
    times = IntField(default=0)
