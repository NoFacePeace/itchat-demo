from hashlib import md5

HOLIDAY = [
    '2018-01-01',
    '2018-02-15',
    '2018-02-16',
    '2018-02-17',
    '2018-02-18',
    '2018-02-19',
    '2018-02-20',
    '2018-02-21',
    '2018-04-05',
    '2018-04-06',
    '2018-04-07',
    '2018-04-29',
    '2018-04-30',
    '2018-05-01',
    '2018-06-16',
    '2018-06-17',
    '2018-06-18',
    '2018-09-22',
    '2018-09-23',
    '2018-09-24',
    '2018-10-01',
    '2018-10-02',
    '2018-10-03',
    '2018-10-04',
    '2018-10-05',
    '2018-10-06',
    '2018-10-07',
]

WORKDAY = [
    '2018-02-11',
    '2018-02-24',
    '2018-04-08',
    '2018-04-28',
    '2018-09-29',
    '2018-09-30',
]

TOKEN = '<token>'

USERNAME = '<username>'

PASSWORD = '<password>'

PASSWORD = PASSWORD.encode('utf-8')

PASSWORD = md5(PASSWORD).hexdigest()