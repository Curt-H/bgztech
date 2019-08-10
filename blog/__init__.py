from blog.models import Users, Session
import uuid
from django.db import models
from django.core.exceptions import ValidationError


def validate_username(username):
    u = username
    # query user from database
    users = Users.objects(username=u)
    print(users)

    if len(users) != 0:
        message = '用户名已被使用'
        raise ValidationError(message)


def set_session(response, user=None):
    session_id = uuid.uuid1().hex

    s = Session().objects(user=user)
    s.session_id = session_id
    s.user = user
    s.save()

    print(session_id)
    response.set_cookie('session_id', s.session_id, max_age=3600)


if __name__ == '__main__':
    set_session('')
