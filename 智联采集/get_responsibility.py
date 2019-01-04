import requests
import single_page_header
from bs4 import BeautifulSoup
responsibility = open('zhilian_job_responsibility.txt','w',encoding='utf-8')
urls =['https://jobs.zhaopin.com/CC311955088J00037153410.htm',
        'https://jobs.zhaopin.com/CC000244625J00080292813.htm']
for url in urls:
    html = requests.get(url,headers=single_page_header.header())
    soup = BeautifulSoup(html.text,'lxml').find(class_="pos-ul")
    responsibility.write(soup.text.strip()+'\n')
print('all spider done')
responsibility.close()
