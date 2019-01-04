import requests
import lxml.html
import random
import re
import time
def run(url):
    # url = 'https://www.kanzhun.com/plc52p10.html?ka=paging10'
    html = requests.get(url,headers=header)
    html_resource = etree.HTML(html.text)
    result = html_resource.xpath('//ul[@class="company_result "]/li')
    for i in result:
        com1_title = i.xpath('div/a[1]/text()')
        com1_review = re.findall(r"\d+\.?\d*",i.xpath('div/a[2]/text()')[0])
        com1_salary = re.findall(r"\d+\.?\d*",i.xpath('div/a[3]/text()')[0])
        com1_interview = re.findall(r"\d+\.?\d*",i.xpath('div/a[4]/text()')[0])
        com1_photo = re.findall(r"\d+\.?\d*",i.xpath('div/a[5]/text()')[0])
        grade_star = re.findall(r"\d+\.?\d*",i.xpath('dl/dd[1]/text()')[0])
        real_salary = re.findall(r"\d+\.?\d*",i.xpath('dl/dd[2]/text()')[0])
        print(com1_title+com1_review+com1_salary+com1_interview+com1_photo+grade_star+real_salary)

if __name__ == '__main__':
    etree = lxml.html.etree
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'aliyungf_tc=AQAAAKA7LWuVdgkA+01Vag8PF1SpAonM; __c=1539575859; W_CITY_S_V=9; AB_T=abva; __g=-; _f_k=reborn; pageType=1; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2F; __t=oGteq7lMg5apg9C; lastMessageId=42003887; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1539575862,1539576023; JSESSIONID=""; isAutoOpenDialog=false; __a=40614890.1539575859..1539575859.59.1.59.59; t=oGteq7lMg5apg9C; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1539577162',
        'Host':'www.kanzhun.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    for num in range(1,2):
        # 设置随机睡眠
        time.sleep(random.randint(2,6))
        url = "https://www.kanzhun.com/plc52p{}".format(num)+".html?ka=paging{}".format(num)
        print(url)
        run(url)