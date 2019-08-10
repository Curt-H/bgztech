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
    namespace = uuid.NAMESPACE_DNS

    s = Session.objects(user=user).first()
    if s is None:
        s = Session()
        session_id = uuid.uuid3(namespace, user.username).hex
        s.session_id = session_id
        s.user = user
        s.save()

        response.set_cookie('session_id', s.session_id, max_age=3600)


if __name__ == '__main__':
    pass
