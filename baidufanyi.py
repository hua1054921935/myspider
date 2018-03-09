# coding=utf-8
import requests
import json
import sys
# from importlib import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')




'''
langList: {
                'zh': '中文',
                'jp': '日语',
                'jpka': '日语假名',
                'th': '泰语','fra': '法语',
                'en': '英语','spa': '西班牙语',
                'kor': '韩语','tr': '土耳其语','vie': '越南语',
                'ms': '马来语','de': '德语',
                'ru': '俄语','ir': '伊朗语',
                'ara': '阿拉伯语','est': '爱沙尼亚语',
                'be': '白俄罗斯语','bul': '保加利亚语',
                'hi': '印地语','is': '冰岛语',
                'pl': '波兰语','fa': '波斯语',
                'dan': '丹麦语',
                'tl': '菲律宾语','fin': '芬兰语',
                'nl': '荷兰语','ca': '加泰罗尼亚语',
                'cs': '捷克语','hr': '克罗地亚语',
                'lv': '拉脱维亚语','lt': '立陶宛语',
                'rom': '罗马尼亚语','af': '南非语','no': '挪威语',
                'pt_BR': '巴西语','pt': '葡萄牙语',
                'swe': '瑞典语','sr': '塞尔维亚语',
                'eo': '世界语','sk': '斯洛伐克语',
                'slo': '斯洛文尼亚语','sw': '斯瓦希里语',
                'uk': '乌克兰语','iw': '希伯来语','el': '希腊语',
                'hu': '匈牙利语','hy': '亚美尼亚语','it': '意大利语',
                'id': '印尼语','sq': '阿尔巴尼亚语','am': '阿姆哈拉语',
                'as': '阿萨姆语','az': '阿塞拜疆语','eu': '巴斯克语','bn': '孟加拉语','bs': '波斯尼亚语','gl': '加利西亚语','ka': '格鲁吉亚语','gu': '古吉拉特语','ha': '豪萨语','ig': '伊博语','iu': '因纽特语','ga': '爱尔兰语','zu': '祖鲁语','kn': '卡纳达语','kk': '哈萨克语','ky': '吉尔吉斯语','lb': '卢森堡语','mk': '马其顿语','mt': '马耳他语','mi': '毛利语','mr': '马拉提语','ne': '尼泊尔语','or': '奥利亚语','pa': '旁遮普语','qu': '凯楚亚语','tn': '塞茨瓦纳语','si': '僧加罗语','ta': '泰米尔语','tt': '塔塔尔语','te': '泰卢固语','ur': '乌尔都语','uz': '乌兹别克语','cy': '威尔士语','yo': '约鲁巴语','yue': '粤语','wyw': '文言文','cht': '中文繁体'    }


'''
# word=input('')
# url='http://fanyi.baidu.com/basetrans'
# postdata={'query':word,
#             'from':'zh',
#             'to':'en'}
#
#
# headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
#
# response=requests.post(url,postdata,headers=headers)
# print(response.json()["trans"][0]["dst"])

class Spider:
    def __init__(self,word):
        self.select_url='http://fanyi.baidu.com/langdetect'
        self.url='http://fanyi.baidu.com/basetrans'
        self.headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
        self.word=word
    def get_post_data(self,language,keys):

        postdata = {'query': self.word,
                'from': language,
                'to': keys}
        print(postdata)
        return postdata

    def select_language(self):
        postdata = {'query': self.word
                    }
        response=requests.post(self.select_url,postdata,headers=self.headers)
        # language=response.json()['lan']
        language=json.loads(response.content.decode())
        language=language['lan']

        return language

    def parse_url(self,postdata):
        response=requests.post(self.url,postdata,headers=self.headers)
        response_data=json.loads(response.content.decode())
        response_data=response_data["trans"][0]["dst"]

        response_data=json.dumps(response_data,ensure_ascii=False,indent=4)
        # return response.json()["trans"][0]["dst"]
        return response_data

    def run(self):
        keys=self.select_lg()
        language=self.select_language()
        postdata=self.get_post_data(language,keys)


        response_data=self.parse_url(postdata)

        print('翻译的结果是：'+response_data)
        # return response_data['trans_result']['data'][0]['dst']

    def select_lg(self):
        lg=input('翻译为什么语言')
        langList={ 'zh': '中文','jp': '日语','jpka': '日语假名','th': '泰语', 'fra': '法语','en': '英语', 'spa': '西班牙语',
                    'kor': '韩语',
                    'tr': '土耳其语', 'vie': '越南语',
                    'ms': '马来语', 'de': '德语',
            'ru': '俄语', 'ir': '伊朗语',
            'ara': '阿拉伯语', 'est': '爱沙尼亚语',
            'be': '白俄罗斯语', 'bul': '保加利亚语',
            'hi': '印地语', 'is': '冰岛语',
            'pl': '波兰语', 'fa': '波斯语',
            'dan': '丹麦语',
            'tl': '菲律宾语', 'fin': '芬兰语',
            'nl': '荷兰语', 'ca': '加泰罗尼亚语',
            'cs': '捷克语', 'hr': '克罗地亚语',
            'lv': '拉脱维亚语', 'lt': '立陶宛语',
            'rom': '罗马尼亚语', 'af': '南非语', 'no': '挪威语',
            'pt_BR': '巴西语', 'pt': '葡萄牙语',
            'swe': '瑞典语', 'sr': '塞尔维亚语',
            'eo': '世界语', 'sk': '斯洛伐克语',
            'slo': '斯洛文尼亚语', 'sw': '斯瓦希里语',
            'uk': '乌克兰语', 'iw': '希伯来语', 'el': '希腊语',
            'hu': '匈牙利语', 'hy': '亚美尼亚语', 'it': '意大利语',
            'id': '印尼语', 'sq': '阿尔巴尼亚语', 'am': '阿姆哈拉语',
            'as': '阿萨姆语', 'az': '阿塞拜疆语', 'eu': '巴斯克语', 'bn': '孟加拉语', 'bs': '波斯尼亚语', 'gl': '加利西亚语', 'ka': '格鲁吉亚语',
            'gu': '古吉拉特语', 'ha': '豪萨语', 'ig': '伊博语', 'iu': '因纽特语', 'ga': '爱尔兰语', 'zu': '祖鲁语', 'kn': '卡纳达语',
            'kk': '哈萨克语', 'ky': '吉尔吉斯语', 'lb': '卢森堡语', 'mk': '马其顿语', 'mt': '马耳他语', 'mi': '毛利语', 'mr': '马拉提语',
            'ne': '尼泊尔语', 'or': '奥利亚语', 'pa': '旁遮普语', 'qu': '凯楚亚语', 'tn': '塞茨瓦纳语', 'si': '僧加罗语', 'ta': '泰米尔语',
            'tt': '塔塔尔语', 'te': '泰卢固语', 'ur': '乌尔都语', 'uz': '乌兹别克语', 'cy': '威尔士语', 'yo': '约鲁巴语', 'yue': '粤语',
            'wyw': '文言文', 'cht': '中文繁体'}
        # keys,values取出的值为字符串类型，需要转换成列表
        # keys=list(langList.keys())[list(langList.values()).index(lg)]
        for (key,value) in langList.items():
            if value==lg:
                keys=key


                return keys


        # print(langList.get('尼泊尔语'))



if __name__ == '__main__':
    word= input('')
    # word='sad'
    a=Spider(word)
    b=a.run()
    # a.select_lg()




# # coding=utf-8
# import requests
# import json
# import sys
#
# class BaiduFanyi:
#     def __init__(self, query_string):
#         self.post_url = "http://fanyi.baidu.com/basetrans"
#         self.query_string = query_string
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}
#
#     def get_post_data(self):  # 准备post数据
#
#         data = {"query": self.query_string,
#                 "from": "zh",
#                 "to": "en"}
#         return data
#
#     def parse_url(self, post_data):  # 发送请求，获取数据
#         response = requests.post(self.post_url, post_data, headers=self.headers)
#         return response.content.decode()
#
#     def get_ret(self, html_str):  # 提取结果
#         dict_ret = json.loads(html_str)
#         ret = dict_ret["trans"][0]["dst"]
#         print("{}的翻译结果是:{}".format(self.query_string,ret))
#
#     def run(self):  # 实现主要逻辑
#         # 1.url，post_data
#         post_data = self.get_post_data()
#         # 2.发送请求，获取数据
#         html_str = self.parse_url(post_data)
#         # 3.提取数据，打印
#         self.get_ret(html_str)
#
# if __name__ == '__main__':
#     query_string = input('')
#     baidu_fanyi = BaiduFanyi(query_string)
#     baidu_fanyi.run()



# url='http://fanyi.baidu.com/langdetect'
# headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
#
# postdata = {'query': '人生'
#                     }
# response=requests.post(url,postdata,headers=headers)
# language=response.json()['lan']
# print(language)