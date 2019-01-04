import os
from bs4 import BeautifulSoup
import time
import re
import pymysql
conn = pymysql.connect(
    user='root', password="9527",
    db='51job', host='localhost')
cursor = conn.cursor()
createTab = """CREATE TABLE IF NOT EXISTS 51job(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    crawl_datetime TEXT NULL,
    post_time TEXT NULL,
    url TEXT NULL,
    company_name TEXT NULL,
    company_size TEXT NULL,
    company_type TEXT NULL,
    job_type TEXT NULL,
    job_name TEXT NULL,
    edu TEXT NULL,
    salary TEXT NULL,
    people_need TEXT NULL,
    walfare TEXT NULL,
    city TEXT NULL,
    workingexp TEXT NULL,
    company_area TEXT NULL,
    work_place TEXT NULL,
    require_content TEXT NULL
    )"""
cursor.execute(createTab)
print('db connect success')
base_dir = 'data_new'
page_number = 1
for txt1 in os.listdir(base_dir):
    try:
        new_dir = base_dir+'/'+txt1
        res = open(new_dir,'r',encoding='utf-8').read()
        require_content1 = BeautifulSoup(res, 'lxml').find(class_="bmsg job_msg inbox").text.replace('\n', '').replace('\t', '')
        # 采集时间、公司名称、任职要求、职位类型、职位名称、福利，工作地址
        crawl_datetime = time.strftime("%Y-%m-%d", time.localtime())
        company_name =BeautifulSoup(res, 'lxml').find(class_="com_name").text.replace('\n', '').replace('\t', '')
        require_content = re.findall('.*职能类别',require_content1)[0].replace('职能类别','')
        job_type = BeautifulSoup(res, 'lxml').find('p',class_="fp").text.replace('\n', '').replace('\t', '').replace('职能类别：','')
        job_name = BeautifulSoup(res, 'lxml').find(class_="cn").h1.text.replace('\n', '').replace('\t', '')
        walfare = BeautifulSoup(res,'lxml').find(class_="jtag").text.replace('\n','')
        work_place =BeautifulSoup(res, 'lxml').find(class_="bmsg inbox").text.replace('\n', '').replace('地图', '')
        # 工资水平、城市、工作经验、学历要求、人数、发布时间
        salary = BeautifulSoup(res, 'lxml').find(class_="cn"e).strong.text.replace('\n', '').replace('\t', '')
        all_info_ = BeautifulSoup(res, 'lxml').find(class_="msg ltype").text.replace('\n', '').replace('\t', '')
        all_info = str(all_info_).split('|')
        city = all_info[0].strip()
        workingexp =all_info[1].strip()
        edu = all_info[2].strip()
        people_need = all_info[3].strip()
        post_time = all_info[4].strip()
        # 企业类型、企业规模、公司业务范围、公司网址
        company_ = BeautifulSoup(res, 'lxml').find(class_="com_tag").text.strip().split('\n')
        company_type = company_[0]
        company_size = company_[1]
        company_area = company_[4]
        url = BeautifulSoup(res, 'lxml').find(class_="com_name").get('href')+'?s=01&t=0'
        # print(crawl_datetime,company_name,job_name,salary,city,workingexp,edu,people_need,post_time,require_content, job_type, walfare,company_type, company_size, company_area, work_place,url)
        sql = "INSERT INTO `51job`(crawl_datetime,company_name,salary,job_name,city,work_place," \
                  "workingexp,edu,people_need,post_time,require_content, job_type, walfare,company_type, company_size, company_area, url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (crawl_datetime,
                             company_name,
                             salary,
                             job_name,
                             city,
                             work_place,
                             workingexp,edu,people_need,post_time,require_content,job_type,walfare,company_type, company_size, company_area, url))
        conn.commit()
        print(page_number)
        page_number += 1
            # file_txt.close()
    except Exception as e:
        pass
