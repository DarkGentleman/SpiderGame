### 爬虫项目练手<br>
项目（八）:scrapy框架爬取股票信息<br>
###### 步骤1：建立工程和Spider模板<br>
* $scrapy startproject BaiduStocks<br>
* $cd BaiduStocks<br>
* $scrapy genspider stocks baidu.com<br>
###### 步骤2：编写Spider<br>
* 配置[stocks.py](https://github.com/DarkGentleman/SpiderGame/blob/master/stocks.py "编写spider")文件<br>
###### 步骤3：编写ITEM Pipelines<br>
* 配置[pipelines.py](https://github.com/DarkGentleman/SpiderGame/blob/master/pipelines.py "编写pipelines")文件<br>
* 配置ITEM_PIPELINES选项，配置[settings.py](https://github.com/DarkGentleman/SpiderGame/blob/master/settings.py "配置ITEM_PIPELINES选项")<br>
###### * * 程序执行——$scrapy crawl stocks<br>

项目（七）：股票信息数据定向爬取。[爬股票数据](https://github.com/DarkGentleman/SpiderGame/blob/master/%E8%82%A1%E7%A5%A8%E6%95%B0%E6%8D%AE%E4%BF%A1%E6%81%AF%E7%88%AC%E5%8F%96.py "爬股票数据")<br>
项目（六）：利用正则表达式爬取淘宝商品信息。[爬淘宝](https://github.com/DarkGentleman/SpiderGame/blob/master/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E7%88%AC%E5%8F%96%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81%E4%BF%A1%E6%81%AF%E6%AF%94%E4%BB%B7.py "仅作技术探讨，请勿不加限制爬取")<br>
项目（一）：爬取豆瓣推荐前250本图书信息（书名、作者、评分、简介），并且生成txt文档保存在本地。[爬豆瓣](https://github.com/DarkGentleman/SpiderGame/blob/master/%E7%88%AC%E5%8F%96%E8%B1%86%E7%93%A3%E6%8E%A8%E8%8D%90%E7%9A%84%E5%A5%BD%E4%B9%A6%E4%BF%A1%E6%81%AF.py "推荐250本好书")<br>
项目（二）：中国大学排名定向爬取（技术路线：requests-bs4）[爬大学排名](https://github.com/DarkGentleman/SpiderGame/blob/master/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D%E5%AE%9A%E5%90%91%E7%88%AC%E5%8F%96.py "不准&太水")<br>
项目（三）：爬取小说《三寸人间》截止更新的全本，保存txt文件到本地。[爬小说](https://github.com/DarkGentleman/SpiderGame/blob/master/%E7%88%AC%E5%8F%96%E5%B0%8F%E8%AF%B4%E3%80%8A%E4%B8%89%E5%AF%B8%E4%BA%BA%E9%97%B4%E3%80%8B%E6%88%AA%E6%AD%A2%E6%9B%B4%E6%96%B0%E7%9A%84%E5%85%A8%E6%9C%AC.py "《三寸人间》")<br>
项目（四）：爬取全本小说《修神外传》并保存txt文件到本地。[爬小说](https://github.com/DarkGentleman/SpiderGame/blob/master/%E7%88%AC%E5%8F%96%E4%B8%8B%E8%BD%BD%E5%85%A8%E6%9C%AC%E5%B0%8F%E8%AF%B4%E3%80%8A%E4%BF%AE%E7%A5%9E%E5%A4%96%E4%BC%A0%E3%80%8B.py "《修神外传》")<br>
项目（五）：网络图片爬取和存储。[爬取图片保存](https://github.com/DarkGentleman/SpiderGame/blob/master/%E7%BD%91%E7%BB%9C%E5%9B%BE%E7%89%87%E7%88%AC%E5%8F%96%E5%92%8C%E5%AD%98%E5%82%A8.py "简单实现")<br>
...
