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

rsp = request.urlopen(baseurl,data=data)
html = rsp.read().decode("utf-8")
print(type(html))
print(html)
json_data = json.loads(html)
for item in json_data['data']:
    print(item['k'],"---",item['v'])