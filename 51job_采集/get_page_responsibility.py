import requests
import single_page_header
from bs4 import BeautifulSoup
import re
# responsibility = open('51_job_responsibility.txt','w',encoding='utf-8')
number = 0
# urls = ['https://jobs.51job.com/jinan/109535254.html?s=01&amp;t=0',
#         'https://jobs.51job.com/kunming/109537060.html?s=01&t=0',
#         'https://jobs.51job.com/jinan/109537030.html?s=01&t=0']
# for url in urls:
for url in open('job_list/job_list.txt','r',encoding='utf-8').readlines():
    try:
        number += 1
        html = requests.get(url,headers=single_page_header.header())
        file_txt = open('data_new/'+str(number)+'.txt','w',encoding='utf-8')
        file_txt.write(html.text)
        print(number)
        file_txt.close()
    except Exception as e:
        pass