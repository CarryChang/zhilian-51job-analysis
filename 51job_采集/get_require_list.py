import requests
import single_page_header
for page in range(1,1000):
    url ='https://search.51job.com/list/000000,000000,0000,32,9,99,%2B,2,{}.html'.format(page)
    para={
        'lang':'c',
        'stype':'1',
        'postchannel':'0000',
        'workyear':'99',
        'cotype':'99',
        'degreefrom':'99',
        'jobterm':'99',
        'companysize':'99',
        'lonlat':'0,0',
        'radius':'-1',
        'ord_field':'0',
        'confirmdate':'9',
        'fromType':'',
        'dibiaoid':'0',
        'address':'',
        'line':'',
        'specialarea':'00',
        'from':'',
        'welfare':'',
    }
    html = requests.get(url,headers=single_page_header.header(),params=para)
    print(html.url)

