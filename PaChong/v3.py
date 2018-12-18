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
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False

    def save_img(self, url, file_name): ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        print('开始保存图片...')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'文件保存成功！')
        f.close()

    def get_pic(self):
        print('开始网页get请求')
        # 使用selenium通过PhantomJS来进行网络请求
        driver = webdriver.PhantomJS()
        driver.get(self.web_url)
        # 执行网页下拉到底部操作，执行5次
        # self.scroll_down(driver=driver, times=2)
        print('开始获取所有a标签')
        all_a = BeautifulSoup(driver.page_source, 'lxml').find_all('img', itemprop='thumbnailUrl')  #获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        # 创建文件夹，并判断是否是新创建
        is_new_folder = self.mkdir(self.folder_path)
        self.mkdir(self.folder_path)  #创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹
        file_names = self.get_files(self.folder_path) #获取文件家中的所有文件名，类型是list
        i = 1
        print("a标签的数量是：", len(all_a)) #这里添加一个查询图片标签的数量，来检查我们下拉操作是否有误
        for a in all_a:
            img_str = a['srcset'] #a标签中完整的style字符串
            print('a标签的srcset内容是：', img_str)
            img_url = img_str.split(',')[2].split(' ')[1]
            width_pos = img_url.index('&w=')
            height_pos = img_url.index('&q=')
            width_str = img_url[width_pos + 3: height_pos]
            height_str = img_url[height_pos + 3: len(img_url)]
            print('高度和宽度数据字符串是：', width_str + '|' + height_str)
            print('截取后的图片的url是：', img_url)

            name_start_pos = img_url.index('photo')
            name_end_pos = img_url.index('?')
            img_name = img_url[name_start_pos: name_end_pos] + '.jpg'
            img_name = img_name.replace('/', '')

            if is_new_folder:
                self.save_img(img_url, img_name)
            else:
                if img_name not in file_names:
                    self.save_img(img_url, img_name)
                else:
                    print("该图片已经存在：", img_name, "，不再重新下载。")

    def scroll_down(self, driver, times):
        for i in range(times):
            print("开始执行第", str(i + 1), "次下拉操作")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行JavaScript实现网页下拉倒底部
            print("第", str(i + 1), "次下拉操作执行完毕")
            print("第", str(i + 1), "次等待网页加载......")
            time.sleep(20)  # 等待20秒（时间可以根据自己的网速而定），页面加载出来再执行下拉操作

    #写一个获取文件夹内所有文件名的方法
    def get_files(self, path):
        pic_names = os.listdir(path)
        return pic_names
beauty = BeautifulPicture()
beauty.get_pic()