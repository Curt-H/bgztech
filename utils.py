import datetime
from time import localtime, strftime


def log(*args):
    t = localtime()
    st = strftime('%Y-%m-%d %I:%M:%S', t)

    print(f'[{st}]:\t', end='')
    print(*args)

    # Dump the log file into a txt file
    with open('log.txt', 'a+', encoding='utf-8') as f:
        print(f'[{st}]:\t', end='', file=f)
        print(*args, file=f)


if __name__ == '__main__':
    log('test')
    log(1, 2, 3, 4)
    log(datetime.datetime.now())
