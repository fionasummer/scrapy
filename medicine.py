#coding=utf-8
import requests
from lxml import etree

url = "https://ypk.familydoctor.com.cn/"
url1 = "https://www.baidu.com"
url2 = "https://www.hao123.com/"


headers1 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",

}
headers={
    # "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
    # "Referer": "https://ypk.familydoctor.com.cn",
}
response = requests.get(url)
res = requests.get(url1,headers=headers)
re = requests.get(url2,headers=headers)
print(response.content)
list_page = response.text
# print(list_page)
html = etree.HTML(list_page)
# print(html)
node_list = html.xpath('//*[@class="sublist"]/dl/dt/a/text()')
node_list6 = html.xpath('//*[@class="sublist"]/dl/dd/a/text()')
node_list1 = html.xpath('//*[@class="clearfix"]/text()')
node_list2 = html.xpath('//*[@id="hotsearch-box"]/div[1]')
# node_list3 =

print(node_list)
print(node_list6)

node = html.xpath('//*[@class="sublist"]/dl')
for i in node :
    children = i.xpath('./dt/a/text()')
    print(children)
    children2 = i.xpath('./dd/a/text()')
    print(children2)
