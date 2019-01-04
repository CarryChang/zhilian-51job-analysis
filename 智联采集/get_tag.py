def get_require(url):
    #          技能要求、 工作地址、工作需求属于第二页的内容
    html = requests.get(url, headers=single_page_header.header())
    soup1 = BeautifulSoup(html.text, 'lxml').find(class_="pos-ul")
    soup2 = BeautifulSoup(html.text, 'lxml').find(class_="add-txt")
    return soup1.text.strip(),soup2.text.strip()
if __name__ == '__main__':
    import json
    import pymysql
    import single_page_header
    import time
    import requests
    from bs4 import BeautifulSoup
    conn = pymysql.connect(
        user='root', password="9527",
        db='zhilian', host='localhost')
    cursor = conn.cursor()
    createTab = """CREATE TABLE IF NOT EXISTS zhilian(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        crawl_datetime TEXT NULL,
        url TEXT NULL,
        company_name TEXT NULL,
        company_size TEXT NULL,
        company_type TEXT NULL,
        job_type TEXT NULL,
        job_name TEXT NULL,
        edu TEXT NULL,        
        empltype TEXT NULL,
        tag TEXT NULL,     
        salary TEXT NULL,     
        city TEXT NULL,
        workingexp TEXT NULL,
        resume_count TEXT NULL,
        company_score TEXT NULL,
        work_place TEXT NULL,
        require_content TEXT NULL
        )"""
    cursor.execute(createTab)
    print('db connect success')
    number = 0
    for i in open('data_json/data_all_json.txt','r',encoding='utf-8').readlines():
        try:
            for i1 in json.loads(i)['data']['results']:
                number += 1
                if number > 32850:
            # 公司名称、企业规模、 公司性质
                    company_name = i1['company']['name']
                    company_size = i1['company']['size']['name']
                    company_type = i1['company']['type']['name']
                    #  职位领域、职位名称、 学历要求、职位类别、职位亮点
                    job_type = i1['jobType']['display']
                    job_name = i1['jobName']
                    edu = i1['eduLevel']['name']
                    empltype = i1['emplType']
                    tag = ''
                    t = str(i1['jobTag']['searchTag'])
                    for i11 in t:
                        tag += str(i11)
                    #      工资水平、 工作经验、福利待遇、城市、简历统计、公司打分
                    salary = i1['salary']
                    city = i1['city']['display']
                    workingexp = i1['workingExp']['name']
                    resume_count = i1['resumeCount']
                    company_score = i1['score']
                    url = i1['positionURL']
                    crawl_datetime = time.strftime("%Y-%m-%d", time.localtime())
                    require_content, work_place = get_require(url)
                # print(crawl_datetime,url,company_name,company_size,company_type,job_type,job_name,edu,empltype,tag,salary,city,workingexp,resume_count,company_score,require_content,work_place)
                    sql = "INSERT INTO `zhilian`(crawl_datetime,url,company_name,company_size,company_type,job_type,job_name,edu,empltype,tag," \
                          "salary,city,workingexp,resume_count,company_score,require_content,work_place) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(crawl_datetime,url,company_name,company_size,company_type,job_type,job_name,edu,empltype,tag,salary,city,workingexp,resume_count,company_score,require_content,work_place))
                    conn.commit()
                    print(number)
        except Exception as e:
            pass


