import requests
from urllib import request,parse
import json

baseurl = 'https://fanyi.baidu.com/sug'
data = {
    'kw':'girl'
}
# data = parse.urlencode(data).encode("utf-8")
headers = {
    'Content-Length':str(len(data))
}

# rsp = request.urlopen(baseurl,data=data)
# html = rsp.read().decode("utf-8")
rsp = requests.post(url=baseurl, data=data, headers=headers)
print(rsp.text)
print(rsp.json())
