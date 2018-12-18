import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os
import time
class BeautifulPicture():
    def __init__(self):  # 类的初始化操作
        self.headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://unsplash.com'  # 要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  # 设置图片要存放的文件目录
    def request(self, url):  #返回网页的response
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象
        return r
    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')
    def save_img(self, url, name): ##保存图片
        print('开始保存图片...')
        img = self.request(url)
        time.sleep(5)
        file_name = name + '.jpg'
        print('开始保存文件')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'文件保存成功！')
        f.close()
    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签')
        all_a = BeautifulSoup(r.text, 'lxml').find_all('img', itemprop='thumbnailUrl')  #获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)  #创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹
        i = 1 #后面用来给图片命名
        print("a标签的数量是：", len(all_a))
        for a in all_a:
            img_str = a['srcset'] #a标签中完整的style字符串
            print('a标签的style内容是：', img_str)
            img_url = img_str.split(',')[2].split(' ')[1]
            width_pos = img_url.index('&w=')
            height_pos = img_url.index('&q=')
            width_str = img_url[width_pos + 3: height_pos]
            height_str = img_url[height_pos + 3: len(img_url)]
            print('高度和宽度数据字符串是：', width_str + '|' + height_str)
            print('截取后的图片的url是：', img_url)
            name_start_pos = img_url.index('photo')
            name_end_pos = img_url.index('?')
            img_name = img_url[name_start_pos: name_end_pos]
            self.save_img(img_url, img_name)
            i += 1

beauty = BeautifulPicture()
beauty.get_pic()