import json
n =0
for i in open('data_json/data_all_json.txt','r',encoding='utf-8').readlines():
    try:
        for i1 in json.loads(i)['data']['results']:
            n +=1
        print(n)
            # print(i1['positionURL'])
    except Exception as e:
        pass
