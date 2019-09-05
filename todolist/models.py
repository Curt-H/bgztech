import time

from mongoengine import *

# Create your models here.
from utils import log


class Todo(Document):
    title = StringField(required=True)
    content = StringField()
    tag = ListField()
    creat_time = IntField(required=True)
    expired_time = IntField()
    repeat = ListField()

    def new(self, data: dict):
        data = data

        self.title = data.get('title', None)
        self.content = data.get('content')
        self.creat_time = time.time()
        self.expired_time = time.time()
        self.tag = data.get('tag', [])
        self.repeat = data.get('repeat', [])
        self.save()
        return 0

    @staticmethod
    def get_data_from_request(request):
        request = request

        data = request.POST.dict()
        tag = request.POST.getlist('tag')
        repeat = request.POST.getlist('repeat')

        data['tag'] = tag
        data['repeat'] = repeat
        return data
