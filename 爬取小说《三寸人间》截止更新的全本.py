# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests , sys

class downloader(object):

    def __init__(self):
        self.server = 'http://www.biquge.com.tw'
        self.target = 'http://www.biquge.com.tw/14_14055/'
        self.names = []
        self.urls = []
        self.nums = 0


    def get_download_url(self):
        resp = requests.get(url = self.target)
        html = resp.text.encode('iso-8859-1')
        soup = BeautifulSoup(html, 'lxml')
        texts = soup.find_all('div', id='list')
        a_bf = BeautifulSoup(str(texts[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[0:])
        for each in a[0:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))


    def get_contents(self, target):
        resp = requests.get(url = target)
        html = resp.text.encode('iso-8859-1')
        soup = BeautifulSoup(html, 'lxml')
        texts = soup.find_all('div', id='content')
        tex = texts[0].text.replace('\xa0' * 8, '\n\n')
        return tex

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《三寸人间》正在下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '《三寸人间》全本.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  Download:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《三寸人间》下载完毕')
