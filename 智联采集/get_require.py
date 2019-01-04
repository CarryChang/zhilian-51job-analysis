import requests
import single_page_header
from bs4 import BeautifulSoup
responsibility = open('get_second/zhilian_job_responsibility.txt','w',encoding='utf-8')
import json
for i in open('data_json/data_all_json.txt','r',encoding='utf-8').readlines():
    for i1 in json.loads(i)['data']['results']:
        url = i1['positionURL']
        html = requests.get(url,headers=single_page_header.header())
        soup = BeautifulSoup(html.text,'lxml').find(class_="pos-ul")
        responsibility.write(soup.text.strip()+'\n')
    print('spider done')
responsibility.close()
