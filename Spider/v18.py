from urllib import request,parse
def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "action": "FY_BY_REALTIME",
        "client": "fanyideskweb",
        "doctype": "json",
        "from": "AUTO",
        "i": "girl",
        "keyfrom": "fanyi.web",
        "salt": "1542535826678",
        "sign": "4a177062fd0708d4f7c48a18bb56bd59",
        "smartresult": "dict",
        "to": "AUTO",
        "typoResult": "false",
        "version": "2.1"
    }
    data = parse.urlencode(data).encode()
    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Language": "zh-CN",
        "Cache-Control": "no-cache",
        "Connection": "Keep-Alive",
        "Content-Length": "200",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=1434187780@10.168.8.61; JSESSIONID=aaaNFDeH7eWJjadXVeMCw; ___rl__test__cookies=1542535826658; OUTFOX_SEARCH_USER_ID_NCOO=1075719494.885307",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    }
    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)

if __name__=="__main__":
    youdao("boy")
