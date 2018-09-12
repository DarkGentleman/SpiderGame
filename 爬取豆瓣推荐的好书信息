# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


#发出请求获得HTML源码的函数
def get_html(url):
    #伪装成浏览器访问
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
55.0.2883.87 Safari/537.36'}
    resp = requests.get(url, headers=headers).text
    return resp

#解析页面，获得数据

def html_parser():
    #调用函数，for循环迭代出所有页面
    for url in all_page():
        soup = BeautifulSoup(get_html(url), 'lxml')
        alldiv = soup.find_all('div', class_='pl2')
        names = [a.find('a')['title'] for a in alldiv]  #书名

        allp = soup.find_all('p', class_='pl')
        authors = [p.get_text() for p in allp]  #作者

        starspan = soup.find_all('span', class_='rating_nums')
        scores = [s.get_text() for s in starspan]  #评分

        sumspan = soup.find_all('span', class_='inq')
        sums = [i.get_text() for i in sumspan]  #简介

        for name, author, score, sum in zip(names, authors, scores, sums):
            name = '书名：' + '《' + str(name) + '》' + '\n'
            author = '作者：' + str(author) + '\n'
            score = '评分：' + str(score) + '/10' + '\n'
            sum = '简介：' + str(sum) + '\n'
            data = name + author + score + sum
            print(data)

            f.writelines(data + '#####################################' + '\n')  #保存数据

#获得所有页面的函数
def all_page():
    base_url = 'https://book.douban.com/top250?start='
    urllist = []
    for page in range(0, 250, 25):
        allurl = base_url + str(page)
        urllist.append(allurl)

    return urllist

filename = '豆瓣好书Top250.txt'
f = open(filename, 'w', encoding='utf-8')
html_parser()
f.close()
print('保存成功')

