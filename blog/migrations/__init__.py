from time import time

from blog.models import Users

if __name__ == '__main__':
    all_users_query = Users.objects()
    all_users = list(Users.objects())
    for user in all_users:
        user.create_time = time()
        user.save()
