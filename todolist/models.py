import time

from mongoengine import *

# Create your models here.
from utils import log


class Todo(Document):
    title = StringField(required=True)
    content = StringField()
    tag = ListField(StringField)
    creat_time = IntField(required=True)
    expired_time = IntField()
    repeat = ListField(IntField)

    def new(self, post: dict):
        post = post

        self.title = post.get('title', None)
        self.content = post.get('content')
        self.tag = []
        self.creat_time = time.time()
        self.expired_time = time.time()
        self.repeat = False
        self.repeat_mark = post.get('repeat')
        self.save()
        return self

    @staticmethod
    def get_data_from_request(request):
        request = request

        data = request.POST.dict()
        tag = request.POST.getlist('tag')
        repeat_mark = request.POST.getlist('repeat')

        data['tag'] = tag
        data['repeat_mark'] = repeat_mark
        return data
