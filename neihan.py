# coding=utf-8

import requests
import time
import re
from lxml import etree



class Spider:
    def __init__(self):
        self.start_url='http://neihanshequ.com/'
        self.url='http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}'
        self.max_time=''
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36','X-CSRFToken':'9303a1f4b25e8f2f68d89b1d0e9cf615','Referer':'http://neihanshequ.com/bar/1/','Cookie':'uuid="w:99d7c4dc60eb4ae09556c6bc9dc6d253"; tt_webid=6529659478042854919; csrftoken=13753cb398583c33da5be8bf0f7727f7; _ga=GA1.2.1382869523.1520304821; _gid=GA1.2.1200588661.1520422263'}

    def get_url(self,max_time):
        url=self.url.format(max_time)

        return url

    def parse_url(self,url):
        response = requests.get(url, headers=self.headers)

        return response

    def save(self,page,data_content):
        with open('neihan.txt', 'a') as f:
            f.write('第%s页段子' %page+ '\n')
            for i in range(0,len(data_content)):
                content=data_content[i]['group']['content']
                f.write('段子'+str(i)+content+'\n')
            print(str(page)+'完成')





    def run(self):
        page=1
        max_time = self.max_time
        while True:
            url=self.get_url(max_time)
            response=self.parse_url(url)
            data=response.json()
            if response:
                data_content = response.json()['data']['data']
                self.save(page,data_content)
                max_time=data['data']['max_time']
                page += 1
            else:
                print('完成')
                break


if __name__ == '__main__':
    a=Spider()
    a.run()