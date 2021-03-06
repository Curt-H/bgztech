from time import localtime, strftime


def log(*args, **kwargs):
    t = localtime()
    st = strftime('%Y-%m-%d %I:%M:%S', t)

    print(f'[{st}]')
    for i in args:
        print(*args)
    for k in kwargs.keys():
        print(f'{k}={kwargs[k]}')

    with open('log.txt', 'a+', encoding='utf-8') as f:
        print(f'[{st}]', file=f)
        print(*args, file=f)
        for k in kwargs.keys():
            print(f'{k}={kwargs[k]}', file=f)


if __name__ == '__main__':
    for i in range(10):
        log('test')
        log('a', c='fuck')
