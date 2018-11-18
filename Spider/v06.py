from urllib import request,parse
import json

baseurl = 'https://fanyi.baidu.com/sug'
data = {
    'kw':'girl'
}
data = parse.urlencode(data).encode("utf-8")
headers = {
    'Content-Length':len(data)
}
req = request.Request(baseurl, data=data, headers=headers)
rsp = request.urlopen(req)
html = rsp.read().decode("utf-8")
print(type(html))
print(html)
json_data = json.loads(html)
for item in json_data['data']:
    print(item['k'],"---",item['v'])