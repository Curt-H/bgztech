# Create your models here.
from mongoengine import *

connect('bgztech')


class Paraphrase(EmbeddedDocument):
    part_of_speech = StringField(required=True)
    paraphrase = StringField(required=True)
    example = StringField()


class Dict(Document):
    word = StringField(required=True, unique=True)
    paraphrase = ListField(EmbeddedDocumentField(Paraphrase))
