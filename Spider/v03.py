from urllib import request
if __name__ == "__main__":
    url = "https://ts.zhaopin.com/jump/index_new.html?utm_source=baiduPC&utm_medium=CPC&utm_term=8804380&utm_content=pp&utm_campaign=pp&utm_provider=partner&sid=121122523&site=u3782246.k95071286716.a24611562822.pb"
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL : {0}".format(rsp.geturl()))
    print("Info : {0}".format(rsp.info()))
    print("Code : {0}".format(rsp.getcode()))

    html = rsp.read()
    html = html.decode()