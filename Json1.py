import json
import urllib.request
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input('Enter-')
data=urllib.request.urlopen(url,context=ctx).read()
info=json.loads(data)
sum=0
for x in info['comments']:
    sum=sum+(int(x['count']))
print(sum)
