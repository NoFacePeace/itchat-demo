# -*- coding: UTF-8 -*-

import requests
import re
from datetime import datetime, timedelta
import itchat

from config import USERNAME, PASSWORD, TOKEN, HOLIDAY, WORKDAY

def getData(date):
    payload = {
        'fp' : TOKEN,
        'username' : USERNAME,
        'pwd' : PASSWORD,   
    }
    session_requests = requests.session()
    login_url = 'http://ssa.jd.com/sso/login?ReturnUrl=http%3A%2F%2Ferp.jd.com%2F'
    result = session_requests.post(
        login_url,
        data = payload,
        headers = dict(referer = login_url)
    )
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    download_url = 'http://pmp.jd.com/leader/daily/exportDailyUserList?orgEid=00a2d658f988870d03ca54ed0d0143f9&listType=.not_filled&paging=true&startSubmitTime=' + date + '&endSubmitTime=' + date
    result = session_requests.get(
        download_url,
        headers = headers
    )
    content = result.content
    content = content.decode(encoding = 'gbk')
    content = content.strip()
    arr = content.split('\n')
    str = ''
    for index in range(1, len(arr)):
        name = re.match('"(.+?)"', arr[index]).group(1)
        if (index % 4 == 0):
            str += '\n'
            str += name + ' '
        else:
            str += name + ' '
    return str
    
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    global datetime
    if msg['Text'] == 'pmp':
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        week = now.weekday()
        len = (week + 3) % 8
        str = ''
        for i in range(0, len):
            datetime = now + timedelta(days = -i)
            week = datetime.weekday()
            date = datetime.strftime('%Y-%m-%d')
            if date not in HOLIDAY:
                if date in WORKDAY:
                    str += date + '\n'
                    str += getData(date)
                    str += '\n'
                elif (week !=5) & (week !=6):
                    str += date + '\n'
                    str += getData(date)
                    str += '\n'
        itchat.send(str, toUserName='filehelper')  

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
