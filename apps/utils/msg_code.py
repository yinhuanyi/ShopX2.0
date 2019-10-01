# coding: utf-8
"""
@Author: Robby
@Module name: msg_code.py
@Create date: 2019-09-29
@Function: 
"""




import random
import datetime
import time
import hashlib
import requests
import json

class WYMSM:
    def __init__(self, mobile, code=None):
        self.mobile = mobile
        self.code = code

    def __get_header(self):
        # appkey = '9038e2fed1d8380f2cc0a10b5d27f674'
        appkey = '18a605bdd94221a910637e2ea80d186b'
        # appsecret = '209cf1b090cf'
        appsecret = 'a8a466273805'

        nonce = random.randint(10000, 100000000)

        ctime = datetime.datetime.utcnow()
        curtime = str(int(time.mktime(ctime.timetuple())))
        s = appsecret + str(nonce) + curtime
        checksum = hashlib.sha1(s.encode('utf-8')).hexdigest()
        Content_Type = "application/x-www-form-urlencoded;charset=utf-8"
        header = {'Content-Type': Content_Type, 'AppKey': appkey, 'Nonce': str(nonce), 'CurTime': curtime,
                  'CheckSum': checksum}
        return header

    def send(self):
        url = 'https://api.netease.im/sms/sendcode.action'
        header = self.__get_header()
        data = {'mobile': str(self.mobile), 'template_id': '14829124'}
        response = requests.post(url=url, data=data, headers=header)
        text = json.loads(response.text)
        print(text)
        return text


if __name__ == '__main__':
    msm = WYMSM('16673103093')
    ret = msm.send()
    code = ret['obj']
    print(code)














