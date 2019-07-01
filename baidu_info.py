#coding=utf-8
import requests
from lxml import etree
import os,sys

import json
# reload(sys)
# sys.setdefaultencoding("utf-8")
class BaiduInfo(object):
    def __init__(self,key_word):
        self.url = "https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%s"%(key_word)
        self.headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

    def get_page(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_list_page(self,list_page):
        html=etree.HTML(list_page)
        node_list = html.xpath('//*[@class="result"]')
        # print node_list
        detail_list=[]
        for node in node_list:
            temp={}
            # try:
            l=node.xpath('./div/p/text()')
            str=""
            # print(l[1:])
            for i in l[1:]:
                str = str+i.replace(' ',"").replace('\t',"").replace('\xa0',"").replace('\n','|')
            li=str.split('|')
            print(li)
            # ['', 'Hicoder', '2019年06月29日10:17', '']
            # ['', '读芯术', '2019年06月29日12:00', '']
            # ['', 'python大大', '2019年06月27日19:35', '']
            # ['', 'python大大', '2019年06月29日11:37', '']
            # ['', 'Excel函数编程可视化', '2019年06月27日06:50', '']

            # except:
                # temp['time']=node.xpath('./div/p/text()')

            # temp['time']=node.find_element_by_xpath('./div/p').text
            # print temp['time'].encoding
            # temp['title']=node.xpath('./h3/')
            # print temp['title']
            # temp['link']=node.xpath('./h3/a/@href')[0]
            # print temp['link']
            # temp['author']=node.xpath('./div[@class="c-summary c-row c-gap-top-small"]/div[@class="c-span18 c-span-last"]/p/text()')
            # print temp['author']
            # temp['desc']=node.xpath('./div[@class="c-summary c-row c-gap-top-small"]/div[@class="c-span18 c-span-last"]/text()')
            detail_list.append(temp)

        try:
            next_url = "https://www.baidu.com"+html.xpath(u'//a[contains(text(),"下一页")]/@href')[0]
            print (next_url)
        except:
            # print "hh"
            next_url=None

        return detail_list, next_url

    def save_data(self,data):
        # with open('info.json','w+') as f:
        #     str_data = json.dumps(data,ensure_ascii=False)+'/n'
        #     f.write(str_data)
        pass

    def run(self):
        next_url = self.url
        while next_url:
            list_page = self.get_page(next_url)
            detail_list, next_url = self.parse_list_page(list_page)
            print (detail_list)

            self.save_data(detail_list)





if __name__ == "__main__":
    bi=BaiduInfo('python')
    bi.run()

# enconding = requests.utils.get_encodings_from_content(response.text)
# # print (enconding)
# html_doc=response.content.decode("utf-8")
# # print (html_doc)
# # with open("new.html", 'wb')as f:
# #     f.write(response.content)
#key_word = sys.argv[1]
# pn = sys.argv[2]
#zx = BaiduInfo(key_word, pn)
# zx.run()