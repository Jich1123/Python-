from urllib import request,parse
from http import cookiejar
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    url = "http://www.renren.com/PLogin.do"
    data = {
        'email':'15151965511',
        'password':'jich921224'
    }
    data = parse.urlencode(data)
    req = request.Request(url,data=data.encode())
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/968794062"
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp1.html","w") as f:
        f.write(html)

if __name__ == "__main__":
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
