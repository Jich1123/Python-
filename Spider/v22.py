import requests
url = "https://www.baidu.com/s?"
kw = {
    "wd": "王八蛋"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
}
rsp = requests.get(url, params=kw, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.status_code)
print(rsp.url)
print(rsp.encoding)