# coding=utf-8
import requests



url='http://www.baidu.com'
proxies={'http':'http://123.125.142.40:80'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36'}
response=requests.get(url,headers=headers,proxies=proxies)

print(response.headers)