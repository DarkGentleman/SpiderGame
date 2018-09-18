import requests
import os
url = 'https://www.nationalgeographic.com/content/dam/environment/2018/09/florence_explainer/01_hurricane_florence_nasa_gettyimages-1030785334.adapt.885.1.jpg'
root = '//home//cai//MOOC图//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取失败')
