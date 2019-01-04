import requests
import list_headers
from bs4 import BeautifulSoup
import re
job_list = open('job_list.txt','a',encoding='utf-8')
# url = 'https://search.51job.com/list/000000,000000,0000,32,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# 1.html?
for page in range(1,1000):
    url ='https://search.51job.com/list/000000,000000,0000,01%252C37%252C38%252C31%252C39,9,99,%2520,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(page)
    html = requests.get(url,list_headers.headers())
    info = BeautifulSoup(html.content,'lxml')
    soup = info.find_all(class_="t1 ")
    for i in soup:
        url = i.find('a').get('href')
        job_list.write(str(url)+'\n')
    print(page)
job_list.close()