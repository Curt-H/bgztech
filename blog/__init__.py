from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from blog.models import Users, Session
import uuid
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

    # find session object, if found, update it, if not create new one
    s = Session.objects(user=user).first()
    if s is None:
        s = Session()
        session_id = uuid.uuid3(namespace, user.username).hex
        s.session_id = session_id
        s.user = user
        s.save()

    response.set_cookie('session_id', s.session_id, max_age=36000)


def current_user(request):
    session_id = request.COOKIES.get('session_id', None)
    print(session_id)

    # if there is no session or expired return 'visivtor'
    if session_id is None:
        print(Users.objects(role='visitor').first())
        return Users.objects(role='visitor').first()
    else:
        session = Session.objects(session_id=session_id).first()
        return session.user.fetch()


def create_user(request):
    result = {}

    # transfer english error msg to Chinese
    error_dict = {
        'This password is too short. It must contain at least 6 characters.': '密码少于6位',
        'This password is too common.': '密码太简单',
        'This password is entirely numeric.': '密码是纯数字'
    }

    # get form data from POST
    post = request.POST
    username = post['username']
    password = post['password']
    try:
        validate_password(password=password)
        validate_username(username)
    except exceptions.ValidationError as error_msg:
        result['success'] = False
        result['error_msg'] = [error_dict.get(e, '未知错误')
                               for e in error_msg]
    else:
        password = make_password(password, 'bgztech')
        u = Users(username=username, password=password)
        u.save()

        result['success'] = True
        result['user'] = u

    return result


def find_user(request):
    post = request.POST
    username = post['username']
    password = post['password']

    user = Users.objects(username=username).first()

    if user is None: return False, user

    return check_password(password, user.password), user


if __name__ == '__main__':
    u = Users()
    u.username = '游客'
    u.password = ''
    u.role = 'visitor'
    u.save()
