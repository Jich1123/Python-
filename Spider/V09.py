from urllib import request,error
if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        '''
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
        req = request.Request(url,headers=headers)
        '''
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0")
        rsq = request.urlopen(req)
        html = rsq.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)