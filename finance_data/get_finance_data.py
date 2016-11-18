# coding=utf-8
import requests
import json
import os
import sys
from pyquery import PyQuery as pq
import re

reload(sys)
sys.setdefaultencoding('utf-8')


# ----------------------------------------------------------------------
def get_stock_code(url):
	""""""
	content = requests.get(url).content
	f = open('code.txt', 'w')
	f.write(content)
	f.close()
	query = pq(content)
	code_collection = str(query('div').filter('.quotebody')('ul')('li').text().encode('utf-8')).split()
	code_patern= re.compile(r'''(.+)\((\d+)\)''')
	
	#for item in code_collection:
		#name_code_group = re.findall(stock_name_code_map, item)
		#if len(name_code_group) > 0:
			#print name_code_group[0][0], name_code_group[0][1]

	name_code=re.co

# ----------------------------------------------------------------------
def get_stock_data(url):
	stock = {'code': '002595'}
	stock_name = '%(code)s' % stock

	if not os.path.isdir(stock_name):
		os.mkdir(stock_name)
	os.chdir(stock_name)

	stock_url = url % stock
	stock_item = ['main', 'each', 'grow', 'pay', 'operate', 'benefit', 'cash']
	for item in stock_item:
		stock_item_url = stock_url + '/' + item + '.txt'
		content = requests.get(stock_item_url).text
		# print stock_item_url
		# print content
		content_json = json.loads(content)
		print content_json
		for key in content_json:
			for item in content_json[key]:
				print item

		f_name = item + '.txt'
		f = open(f_name, 'w')
		f.write(str(content))
		f.close()
	# print stock_item_url


if __name__ == '__main__':
	if not os.path.isdir('stock_data'):
		os.mkdir('stock_data')
	os.chdir('./stock_data')

	print 'get stock code'
	url = r'''http://quote.eastmoney.com/stocklist.html'''
	get_stock_code(url)

# url = r'''http://stockpage.10jqka.com.cn/basic/%(code)s'''
# get_stock_data(url)
# print 'here'
