# coding=utf-8

import requests
from lxml import etree
import re
import json
from queue import Queue
import threading

class QiushiSpider:
    def __init__(self):
        self.proxies={'http':'http://89.236.17.108:3128'}
        self.url='https://www.qiushibaike.com/8hr/page/{}/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        self.url_queue=Queue()   # 放的是url
        self.get_content_list_queue=Queue()  # 放的是
        self.save_queue=Queue()
    def get_url_list(self):
        for i in range(1,14):
            self.url_queue.put(self.url.format(i))




    def parse_url(self):
        while True:
            url=self.url_queue.get()
            response=requests.get(url,headers=self.headers,proxies=self.proxies)
            # print(response.content.decode())
            self.get_content_list_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            content=self.get_content_list_queue.get()
            html=etree.HTML(content)
            content_list=html.xpath('//div[contains(@class,"article block untagged mb15")]')
            content_lists=[]
            for content in content_list:
                contents=content.xpath('.//div[@class="content"]//span/text()')
                content_lists.append(contents)
            print(content_lists)
            self.save_queue.put(content_lists)
            self.get_content_list_queue.task_done()
            # return content_lists

    def save(self):
        while True:
            data=self.save_queue.get()
            with open('糗事.txt','a') as f:
                for datas in data:
                    f.write('文本')
                    # print(datas)
                    f.write(datas[0])
                    f.write('\n')
                self.save_queue.task_done()


    def run(self):
        # 1.threadlis
        threaddlist=[]
        r_url=threading.Thread(target=self.get_url_list)
        threaddlist.append(r_url)
        # 2. 遍历发送请求
        for i in range(3):
            t_parse=threading.Thread(target=self.parse_url)
            threaddlist.append(t_parse)
        #  3.获取数据列表
        t_content=threading.Thread(target=self.get_content_list)
        threaddlist.append(t_content)

        #  4.保存
        t_save=threading.Thread(target=self.save)
        threaddlist.append(t_save)
        for t in threaddlist:
            t.setDaemon(True)
            t.start()
            # t.join()

        for q in [self.url_queue,self.get_content_list_queue,self.save_queue]:
            q.join()

        print('主进程结速')



if __name__ == '__main__':
    a=QiushiSpider()
    a.run()