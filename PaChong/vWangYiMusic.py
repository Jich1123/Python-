import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
import os
import time

class BeautifulPicture():

    def __init__(self):  # 类的初始化操作
        self.headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://music.163.com/#/artist/album?id=101988&limit=150&offset=0'  # 要访问的网页地址
        self.folder_path = 'D:\ALL_MUSIC'  # 设置图片要存放的文件目录

    def save_img(self, url, file_name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()


    def request(self, url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r


    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False


    def get_files(self, path):  # 获取文件夹中的文件名称列表
        pic_names = os.listdir(path)
        return pic_names

    def spider(self):
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        self.mkdir(self.folder_path)  # 创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹
        file_names = self.get_files(self.folder_path)  # 获取文件夹中的所有文件名，类型是list


        all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        print("总数:", len(all_li))
        for li in all_li:
            album_img = li.find('img')['src']
            album_name = li.find('p', class_='dec')['title']
            album_date = li.find('span', class_='s-fc3').get_text()
            end_pos = album_img.index('?')  # 找到问号的位置
            album_img_url = album_img[:end_pos]  # 截取问号之前的内容
            photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
            print(album_img_url, photo_name)

            if photo_name in file_names:
                print('图片已经存在，不再重新下载')
            else:
                self.save_img(album_img_url, photo_name)

music = BeautifulPicture()
music.spider()