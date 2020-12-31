#!/usr/bin/python
# coding: utf-8

import macros
import sys
import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

channel = sys.argv[1]
xml_file = channel + '.xml'

index_page = '' + macros.head
links = macros.tail

tree = ET.parse(xml_file)
root = tree.getroot()


def get_content(text, link):
	response = requests.get(link)
	text = response.text.encode('utf-8')
	parser = BeautifulSoup(text, 'html.parser')

	for img in parser.find_all('img'):
		del img['width']
		del img['height']
	for script in parser.find_all('script'):
		script.decompose()
	for style in parser.find_all('style'):
		style.decompose()
	for zoom in parser.find_all("div", attrs = {'id': 'zoomattribute'}):
		zoom.decompose()
	for zoom in parser.find_all("div", attrs = {'class': 'zoomattribute'}):
		zoom.decompose()
	for ext_link in parser.find_all("ul"):  #, attrs = {'class': 'external-link'}):
		ext_link.decompose()

	headerimg = parser.find('div', id='headerimg')
	if headerimg is None:
		headerimg = ''
	else:
		headerimg = headerimg.prettify().encode('utf-8') + '\n<hr/>\n' + macros.proxy
	storytext = parser.find('div', id='storytext').prettify().encode('utf-8') 
	return headerimg + storytext


def write_page(f_name, f_path, title, link, content):
	new_link = macros.git_base_url + '/' + channel + '/' + f_name 
	body = '### ' + title
	body += "\n------------------------\n\n" + macros.menu + "\n\n" +  content
	body += "\n<hr/>\n手机上长按并复制下列链接或二维码分享本文章：<br/>"
	body += "\n" + new_link + " <br/>"
	body += "\n<a href='" + new_link + "'><img src='" + new_link + ".png'/></a> <br/>"
	body += "\n原文地址（需翻墙访问）：" + link + "\n"
	body += "\n\n------------------------\n" + links
	fh = open(f_path, 'w')
	fh.write(body)
	fh.close()


def get_name(link):
	fname = link.split('/')[-1]
	return fname.split('.')[0]


for child in root[0]:
	if child.tag != 'item':
		continue
	link = child.find('guid').text
	title = child.find('title').text.encode('utf-8')
	#content = child.find('content').text.encode('utf-8')
	#content = get_content(content)
	name = get_name(link) + '.md'
	file_path = '../pages/' + channel + '/' + name 
	
	#if True: 
	if not os.path.exists(file_path):
		print file_path
		content = child.find('content').text.encode('utf-8')
		content = get_content(content, link)
		macros.write_page(channel, name, file_path, title, link, content)
		#print content
	index_page += '#### [' + title + '](' + file_path + ') \n'


index_file = open('../indexes/' + channel + '.md', 'w')
index_file.write(index_page)
index_file.close()


