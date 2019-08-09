from blog.models import Users
from django.core.exceptions import ValidationError


def validate_username(username):
    u = username
    # query user from database
    users = Users.objects(username=u)
    print(users)

    if len(users) != 0:
        message = '用户名已被使用'
        raise ValidationError(message)
