import urllib.request
import urllib.parse
import json
import time

while True:
    
    content = input("Please input the content which you need to translate. Enter 'q' to quit: ")
    if content[0].lower() == 'q':
        break
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    #head = {}
    #head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.95 Safari/537.4'

    data={}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'

    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.95 Safari/537.4')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print("Translate Results: %s " %(target['translateResult'][0][0]['tgt']))
    time.sleep(5)
