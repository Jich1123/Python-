with open(r"test02.txt", 'w', encoding='utf-8') as f:
    f.write("生活不止眼前的苟且，\r\n 还有诗和远方的田野")
    f.writelines("是吗？")

with open(r"test02.txt", 'w', encoding='utf-8') as f:
    l = ["I","LOVE","YOU"]
    f.writelines(l)