from urllib import request,error
if __name__ == "__main__":
    url = "http://www.baiduddddddddddddd.com"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req).read()
        html = rsp.decode()
        print(html)
    except error.URLError as e:
        print("URLError:{0}",e.reason)
        print("URLError:{0}",e)
    except Exception as e:
        print(e)