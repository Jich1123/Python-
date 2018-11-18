from urllib import request
if __name__ == "__main__":
    url = "http://www.renren.com/968794062"
    headers = {
        "Cookie":"anonymid=jomlbluanwr44s; depovince=GW; jebecookies=7162e259-2fa4-40fc-94db-57e27d56e349|||||; _r01_=1; JSESSIONID=abcBJTjpgUd4P867m1LCw; ick_login=14337bd9-ffe5-48a9-a41c-82b1c3484d85; jebe_key=cc3545de-d098-4aae-81af-168a7bdefc9a%7C86b61d86aa69ce9485f8ba8f89131f93%7C1542528220058%7C1; ick=5e0d0bcc-82c5-499d-8d60-8eecfff80710; t=716dab263150fdddc154ac43df7239e02; societyguester=716dab263150fdddc154ac43df7239e02; id=968794062; xnsid=da2a3538; XNESSESSIONID=7ebe4ebbb9a5; WebOnLineNotice_968794062=1; ver=7.0; loginfrom=null; wp_fold=0"
    }
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    with open("rsp.html","w") as f :
        f.write(html)