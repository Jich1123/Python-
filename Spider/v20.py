'''
    ajax实验
'''
from urllib import request
import json
url = "https://movie.douban.com/j/chart/top_list?type=20&interval_id=100:90&action=&start=160&limit=20"
rsp = request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)
print(data)