# coding=utf-8
import requests
from lxml import etree
import pymysql
import json
# url='http://218.97.241.83/web/manage.php?act=login'
# urls='http://218.97.241.83/web/ucenter.php?id=1'
# headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# # response=requests.get(urls,headers=headers)
# data={'username':'lansing',
# 'password':'123456'}
# proxy={'http':'http://89.236.17.108:3128'}
# session=requests.session()
# session.post(url,headers=headers,data=data,proxies=proxy)
#
# responses=requests.get(urls,headers=headers,proxies=proxy)
# html=responses.content
# htm_data=etree.HTML(html)
# user_list=htm_data.xpath('//span[@class="val"]/text()')
# print(user_list)
# username=user_list[0]
# sex=user_list[1]
# age=user_list[2]
# email=user_list[3]
# phone=user_list[4]



class Login:
    def __init__(self):
        self.url='http://218.97.241.83/web/manage.php?act=login'
        self.urls='http://218.97.241.83/web/ucenter.php?id=1'
        self.headers=headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36'}
        self.data={'username':'lansing','password':'123456'}
        self.proxies={'http':'http://89.236.17.108:3128'}
    def parse_url(self,url):
        response=requests.get(url,headers=self.headers,proxies=self.proxies)
        return response

    def get_data(self,response):
        html = response.content
        htm_data = etree.HTML(html)
        user_list = htm_data.xpath('//span[@class="val"]/text()')
        username = user_list[0]
        sex = user_list[1]
        age = user_list[2]
        email = user_list[3]
        phone = user_list[4]

        return username,sex,age,email,phone
    def save(self,username, sex, age, email, phone):
        # 建立连接
        connect=pymysql.Connect( host='localhost',
                                    port=3306,
                                    user='root',
                                    passwd='mysql',
                                    db='python01',
                                    charset='utf8')

        '''
          create table message(
                  id int primary key auto_increment,
                  username varchar(18),
                  sex varchar(100),
                  age INT (2),
                  email VARCHAR (100),
                  phone VARCHAR(100)
            );
        '''
        cursor = connect.cursor()

        # age=json.dumps(age,ensure_ascii=False)
        # print(age)
        sql = "INSERT INTO message (username, sex, age,email,phone) VALUES ( '%s', '%s', '%s','%s','%s')"
        data = (username, sex,age,email, phone)
        cursor.execute(sql % data)
        connect.commit()
        print('成功')




    def run(self):
        #1.发送post请求设置session
        session = requests.session()
        session.post(self.url, headers=self.headers, data=self.data,proxies=self.proxies)
        #2.发送get请求
        response=self.parse_url(self.urls)
        username, sex, age, email, phone=self.get_data(response)
        self.save(username, sex, age, email, phone)



if __name__ == '__main__':
    a=Login()
    a.run()





