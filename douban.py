# coding=utf-8
import sys
import requests
import json


class Spider:
    def __init__(self):
        self.page=0
        self.list1=[]
        self.urls='https://movie.douban.com/j/subject_abstract?subject_id='
        self.url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Referer': 'https://movie.douban.com/tv/'}
        # self.cookies = {
        #     'Cookie': 'll="108288"; bid=zJ6_IE4YJPs; __yadk_uid=dXedEOwhPpeujAxOtTlWahErIdVyyCR8; ps=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1520250625%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=D28A998D8D35CEA5B8917979CDE7E2B78|c0bb42fd1e169790f98aa393c57053b9; dbcl2="174990972:cEJ9tAkDwGA"; ck=tgN7; _pk_id.100001.4cf6=764b44f6f6fc2e3b.1519965183.2.1520250977.1519965183.; _pk_ses.100001.4cf6=*; __utma=30149280.1765861777.1520249626.1520249626.1520249626.1; __utmb=30149280.1.10.1520249626; __utmc=30149280; __utmz=30149280.1520249626.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1081436369.1520250927.1520250927.1520250927.1; __utmb=223695111.0.10.1520250927; __utmc=223695111; __utmz=223695111.1520250927.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0'}


    def response(self,url):
        response = requests.get(url, headers=self.headers)

        return response

    def movie_list_id(self):
        while True:
            response_data=self.response(self.url+str(self.page*20))
            movie_list = response_data.json()['subjects']
            if movie_list:
                for movie in movie_list:
                    self.list1.append(movie['id'])
                #
                self.page += 1

            else:
                # print(self.list1)
                break
        return self.list1

    def movie_info(self):
        with open('电视剧.txt', 'a') as f:
            for id in self.movie_list_id():
                response_data=self.response(self.urls+id)
                response_data=json.loads(response_data.content.decode())
                print(response_data)
                movie=response_data['subject']
                data = json.dumps(movie, ensure_ascii=False)
                print(data)
                f.write(data)
                f.write('\n')




if __name__ == '__main__':
    a=Spider()
    a.movie_info()