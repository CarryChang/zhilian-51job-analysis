# coding=utf-8
import requests
import list_headers
import json
import time
data_demo= open('data_json/data_all_json.txt','w',encoding='utf-8')
# # 全国 page = 0,90,180,270
area = ['489']
# 全部的学历类别，互联网全类别
for are in area:
    # 10800条数据
    for page in range(1200):
        data = {
            # 'start': '90',
            'start': 90*page,
            'pageSize': '90',
            'cityId': are,
            'industry': '10100',
            'workExperience': '-1',
            'education': '-1',
            'companyType': '-1',
            'employmentType': '-1',
            'jobWelfareTag': '-1',
            'kt': '3',
        }
        # 采集json
        url = 'https://fe-api.zhaopin.com/c/i/sou'
        time.sleep(1)
        html = requests.get(url,params=data,headers=list_headers.headers())
        print(page)
        data_demo.write(json.dumps(html.json()))
        data_demo.write('\n')
data_demo.close()

