# coding=utf-8
import requests
# url='http://mail.sina.com.cn/cgi-bin/sla.php'
url='https://passport.baidu.com/v2/api/?login'
url_provie='https://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid='
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.84 Safari/537.36'}
# Cookie='SINAGLOBAL=2505105927709.9565.1508154738426; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; login_sid_t=e44710e918828d9516802e8d876b15b2; cross_origin_proto=SSL; YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; WBStorage=c5ff51335af29d81|undefined; _s_tentry=passport.weibo.com; Apache=2290769423482.9565.1519988636778; ULV=1519988636789:9:1:1:2290769423482.9565.1519988636778:1515759312627; SCF=AgfE6scUsGmz8dJ8wAG85n16T_C1lC9kW76JiPhIJ05fNr9zjWifL4LDh4v6yz8b0Crp00dj_cBScvvGbW5lKhE.; SUB=_2A253nV-JDeRhGeNP7FES8irNyTSIHXVU6zZBrDV8PUNbmtBeLVTHkW9NTn4UAXz4I_xIZ3X26RHQwy811Ez5k-RX; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhyjyvM2XCcgY7zyBfaA1kn5JpX5KzhUgL.Fo-pS0e0eoBpeon2dJLoIEXLxKqL1KMLBK.LxK-LB--L1h.LxKBLBonL12zLxK.L1-zLB-2LxK-LBKBLBK.t; SUHB=0sqRFUPzaNjYsH; ALF=1551524697; SSOLoginState=1519988697; wvr=6; YF-Page-G0=c704b1074605efc315869695a91e5996; UOR=,,login.sina.com.cn'
# cookies=dict(cookies=Cookie)
# # 实例化session对象
# session=requests.session()
# response=session.get(url,cookies=cookies,headers=headers)
# print(response.content.decode())
url_data={'userName':'15617681261','password':'hua6754358'}


session=requests.session()
session.post(url,data=url_data,headers=headers)

response=requests.get(url_provie,headers=headers)
with open('a.html','wb') as f:
    f.write(response.content)



