from django.shortcuts import redirect

from blog import current_user, get_from_cookies
from utils import log


def bgz_checked(F):
    def wrapper(request):
        log('开始验证用户权限')
        session_id = get_from_cookies(request, 'session_id')
        u = current_user(session_id)

        if u.username == 'BGZ':
            log(f'验证通过, 用户{u.username}')
            return F(request)
        log(f'验证失败, 拒绝访问, {u.username}没有权限')
        return redirect('/signin')

    return wrapper
