import json

def get_company(i1):
    # 公司名称、企业规模、 公司性质
    print(i1['company']['name'],i1['company']['size']['name'], i1['company']['type']['name'], i1['company']['url'])

def get_job(i1):
    #  职位领域、职位名称、 学历要求、职位类别、职位亮点
    print(i1['jobType']['display'],i1['jobName'], i1['eduLevel']['name'],i1['emplType'],i1['jobTag']['searchTag'])
for i in open('data_demo.txt','r',encoding='utf-8').readlines():
    for i1 in json.loads(i)['data']['results']:
        print(i1)
        # get_job(i1)
        #      工资水平、 工作经验、福利待遇、城市
        # print(i1['salary'],i1['welfare'],i1['city']['display'],i1['workingExp']['name'])
        # get_company(i1)
#           职位信息、工作地址、工作需求

