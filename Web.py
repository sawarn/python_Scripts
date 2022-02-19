import urllib.request
import ssl
import xml.etree.ElementTree as ET
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input('Enter-')
xml=urllib.request.urlopen(url,context=ctx).read()
data=ET.fromstring(xml)
data_lst=data.findall('.//count')
sum=0
for x in data_lst:
    sum=sum+int(x.text)
print(sum)
