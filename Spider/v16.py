from urllib import request,parse
from http import cookiejar
cookie = cookiejar.MozillaCookieJar()
cookie.load("cooki.txt",ignore_expires=True,ignore_discard=True)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler,https_handler,cookie_handler)


def getHomePage():
    url = "http://www.renren.com/968794062"
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp2.html","w") as f:
        f.write(html)

if __name__ == "__main__":
    getHomePage()