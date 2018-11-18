from urllib import request,error
if __name__ == "__main__":
    url = "http://116.196.112.60/asdf"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req).read()
        html = rsp.decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPError:{0}",e.reason)
        print("HTTPError:{0}",e)
    except error.URLError as e:
        print("URLError:{0}",e.reason)
        print("URLError:{0}",e)
    except Exception as e:
        print(e)