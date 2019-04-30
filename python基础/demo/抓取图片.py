#coding=UTF-8

#导入库
import pip
pip.main(["install","bs4"])
pip.main(["install","requests"])
pip.main(["install","lxml"])

from bs4 import BeautifulSoup
import requests

import os

# config 抓取地址


ConfigBaseUrl = "http://www.onn9.com/?p="
ConfigPerson = "18766"
ConfigPages = 2
ConfigDivKey = "class"
ConfigDivValue =  "single-content"


# 抓取地址集合
URLS = []
for i in range(1,ConfigPages):
	 if i==1:
	 	 str_i = ""
	 else:
	 	 str_i ="_"+ str(i)

	 item = ('%s%s'  %  (ConfigBaseUrl,ConfigPerson))
	 URLS.insert(i,item)

print(URLS)

# 遍历抓取
for URL in URLS:
	# 抓取该URL的内容
	html = requests.get(URL).text
	print(URL)
	html = requests.get(URL).text

	#解析html，并存放在soup中
	soup = BeautifulSoup(html, 'lxml')
	#找到目标div
	img_ul = soup.find_all('div', {ConfigDivKey: ConfigDivValue})

	#创建img文件夹来存放图片
	dir = 'D:/huawei/img'+ConfigPerson+"/"
	if not os.path.exists(dir):
		os.makedirs(dir)

	#循环遍历所有img
	imgs = []
	for ul in img_ul:
		img_item = ul.find_all('img')
		imgs+=img_item

	print(imgs)

	#一一访问图片并下载
	for img in imgs:
	    url = img['data-original']
	    r = requests.get(url, stream=True)
	    image_name = url.split('/')[-1]
	    with open('%s%s' % (dir, image_name),'wb') as f:
	        for chunk in r.iter_content(chunk_size=128):#以128字节大小存放
	            f.write(chunk)
	    print('Saved %s' % image_name)
