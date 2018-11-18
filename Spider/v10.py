from urllib import request,error
if __name__ == "__main__":
    url = "http://www.cnblogs.com/anzhangjun/p/8495184.html"

    proxy = {'http':'183.3.150.210:41258'}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e :
        print(e)
    except error.URLError as e :
        print(e)
    except Exception as e :
        print(e)