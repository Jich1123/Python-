try:
    fh = open("test.txt","w")
    fh.write("这是一个测试文件")
except IOError:
    print("没有找到这个文件！")
else:
    print("写入成功！")
    fh.close()