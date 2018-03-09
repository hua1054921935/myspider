
# coding=utf-8
import requests
from lxml import etree
import json
# name=input()
# url='https://tieba.baidu.com/f?ie=utf-8&kw='+name+'&pn={}'
# headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}
#
#
# page=0
#
# with open('贴吧1.txt','a') as f:
#     while True:
#         urls=url.format(str(page*50))
#
#         response = requests.get(urls, headers=headers)
#
#
#         if response:
#             html=etree.HTML(response.content)
#
#             # 先分组
#             list_li = html.xpath('//li[contains(@class,"tl_shadow tl_shadow_new")]')
#
#             for list_lis in list_li:
#                 data_urls = list_lis.xpath('./a/@href ')
#                 # print(data_urls)
#                 title=list_lis.xpath('.//div[@class="ti_title"]/span/text()')
#                 # print(title)
#                 img_url=list_lis.xpath('.//img[@class="j_media_thumb_holder medias_img medias_thumb_holder"]/@data-url')
#                 # print(img)
#                 # content=list_lis.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')
#                 a=dict(title=title,url=data_urls,img_url=img_url)
#                 # print(a)
#                 f.write(json.dumps(a,ensure_ascii=False)+'\n')
#                 # print(a)
#             print('第%s页完成' %page)
#             page+=1
#         else:
#             print('完成')
#             break


class Spider:
    def __init__(self,name):
        self.name=name
        self.headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'}
        self.url='http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}'.format(name)
        self.urls='http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/'

    #     发起请求，获取响应
    def parse_url(self,url):


        response = requests.get(url, headers=self.headers)

        return response.content

    def get_list_url(self,response):
        html = etree.HTML(response)

        # 先分组
        list_li = html.xpath('//li[contains(@class,"i")]')
        content_list=[]
        for div in list_li:
            content={}
            content['title']=div.xpath('./a/text()') if len(div.xpath('./a/text()')) >0 else None
            content['href']=self.urls+div.xpath('./a/@href') if len(div.xpath('./a/@href'))>0 else None
            content['img_list']=

    def get_detail_img(self,detail_url,img_list):
        # 1.请求详情页
        detail_html_str=self.parse_url(detail_url)
        # 2.提取第一页图片
        detail_html=etree.HTML(detail_html_str)
        img_list.extent(detail_html.xpath("//img[@class='BDE_Image']/@src"))
        # 3.获取下一页url
        next_url=detail_html.xpath("//a[text()='下一页']/@href")
        if len(next_url)>0:
            return  self.get_detail_img(next_url)
        #循环1--3


        return list_li

    def get_data(self,list_li):
        for list_lis in list_li:
            data_urls = list_lis.xpath('./a/@href ')
            # print(data_urls)
            title = list_lis.xpath('.//div[@class="ti_title"]/span/text()')
            # print(title)
            img_url = list_lis.xpath('.//img[@class="j_media_thumb_holder medias_img medias_thumb_holder"]/@data-url')
            # print(img)
            # content=list_lis.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')
            dict_data = dict(title=title, url=data_urls, img_url=img_url)
            # print(a)
            return dict_data

    def save_data(self,dict_data):
        with open('贴吧1.xml', 'a') as f:
            f.write(json.dumps(dict_data, ensure_ascii=False) + '\n')
            print()



    def run(self):

        while True:


            response=self.parse_url(url)
            if response:
                list_li=self.get_list_url(response)
                data=self.get_data(list_li)
                self.save_data(data)
                print('第%s页完成' % self.page)
                self.page+=1
            else:
                print('结束')
                break



if __name__ == '__main__':
    name=input('贴吧名')
    spi=Spider(name)
    spi.run()








