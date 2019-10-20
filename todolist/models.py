import time

from mongoengine import *

# Create your models here.
from utils import log


class Todo(Document):
    title = StringField(required=True)
    content = StringField()
    tag = ListField()
    create_time = IntField(required=True)
    expired_time = IntField()
    repeat = ListField()
    uuid = UUIDField()

    def new(self, data: dict):
        data = data

        self.title = data.get('title', 'No title')
        self.content = data.get('content', 'No Content')
        self.create_time = data.get('create_time')
        self.expired_time = data.get('expired_time')
        self.tag = data.get('tag', [])
        self.repeat = data.get('repeat', [])
        self.save()
        return 0

    @staticmethod
    def get_data_from_request(request):
        request = request

        # Get the list element in QueryDict object
        data = request.POST.dict()
        tag = request.POST.getlist('tag')
        repeat = request.POST.getlist('repeat')

        # Change expired time into int from string
        create_time = time.time()
        expired_time = float(data.get('duration')) * 3600 * 24 + create_time

        data['tag'] = tag
        data['repeat'] = repeat
        data['create_time'] = create_time
        data['expired_time'] = expired_time

        return data
