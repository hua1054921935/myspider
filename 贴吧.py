# coding=utf-8

import requests
import os

# word=input('关键字')
#
# page=0
# os.chdir('tieba')
# while page<=20:
#     url='https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(word,page*50)
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36'}
#
#     filename=page
#
#     response=requests.get(url,headers)
#
#     with open(str(filename)+'.html','wb') as f:
#         f.write(response.content)
#     print('保存成功')
#     page += 1


# 面向对象
class Spider:
    def __init__(self,word):
        self.url='https://tieba.baidu.com/f?kw='+word+'&ie=utf-8&pn={}'

        self.page=1
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36'}
    def get_url_list(self):#获取url

        return [self.url.format(self.page for i in range(0,20))]
    def get_response(self):
        url=self.get_url()
        response=requests.get(url,heades=self.headers)
        return response


    def run(self):
        #
        pass









