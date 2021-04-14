import time

if __name__ == '__main__':
    with open('today.txt', 'wt') as fin:
        fin.write(time.ctime(time.time()))

    today_string = ''
    with open('today.txt', 'rt') as fout:
        today_string = fout.readline()

    print(today_string)

    time_pars = time.strptime(today_string)
    print(time_pars)

    import datetime
    birthday = datetime.date(1999, 12, 12)
    print(birthday.day)
    print(birthday + datetime.timedelta(days = 10000))
