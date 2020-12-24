import calendar


def twentieth_century_sundays():
    m = []
    for j in range(1901, 2001):
        for i in range(1, 13):
            m.append(calendar.weekday(j, i, 1))
    return m.count(6)


def run():
    print(twentieth_century_sundays())
    print(calendar.weekday(1900, 1, 1))
    print(calendar.calendar(1901))
    print(calendar.calendar(1902))

