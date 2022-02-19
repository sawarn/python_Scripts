import json
import urllib.request,urllib.error,urllib.parse
import ssl
api_key = False
if api_key is False:
    api_key=42
    servurl='http://py4e-data.dr-chuck.net/json?'
else:
    servurl='https://maps.googleapis.com/maps/api/geocode/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    add=input('Enter location:')
    if len(add)<1:
        break
    parms = dict()
    parms['address'] = add
    if api_key is not False: parms['key'] = api_key
    url = servurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    try:
        js = json.loads(str(data))
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    Pid= js["results"][0]["place_id"]
    print(Pid)
