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

def get_content(orgText, link):
	text = orgText.replace('</p>\n</p>','</p>')
	parser = BeautifulSoup(text, 'html.parser')
	for img in parser.find_all('img'):
		del img['width']
		del img['height']
	for iframe in parser.find_all('iframe'):
		iframe.decompose()
	for script in parser.find_all('script'):
		script.decompose()
	for a in parser.find_all('a'):
		del a['title']
		del a['class']
	content = '<div>' + parser.prettify().encode('utf-8')  + '</div>'

	# get post image
	response = requests.get(link)
	text = response.text.encode('utf-8')
	parser = BeautifulSoup(text, 'html.parser')
	post_image = parser.find('div', attrs = {'class': 'featured_image'})
	if post_image is None:
		post = ''
	else:
		#img = post_image.find('img')
		img = post_image.find('noscript').find('img')
		caption = post_image.find('div', attrs = {'class': 'caption'})
		if img is None or caption is None:
			post = ''
		else:
			del img['width']
			del img['height']
			post = '<div>' + img.prettify().encode('utf-8') + \
				caption.prettify().encode('utf-8') + '</div><hr/>' + macros.proxy

	#.replace('<a href', '<span href').replace('</a>', '</span>') \
	return (post + content ) \
		.replace('<a href', '<ok href').replace('</a>', '</ok>') \
		.replace('</figure>','</figure><br/>') \
		.replace('<figcaption','<br/><figcaption') \
		.replace('</figcaption>','</figcaption><br/>') \
		.replace('<h2>', '<h4>') \
		.replace('<h2 ', '<h4 ') \
		.replace('</h2>', '</h4>')


def get_name(link):
	fname = link.split('/')[-1]
	return fname.split('.')[0]


def keep_updating(title):
	return title.find('更新') > -1


for child in root[0]:
	if child.tag != 'item':
		continue
	link = child.find('link').text
	title = child.find('title').text.encode('utf-8')
	#content = child.find('content').text.encode('utf-8')
	#content = get_content(content)
	name = get_name(link) + '.md'
	file_path = '../pages/' + channel + '/' + name 
	
	if not os.path.exists(file_path) or keep_updating(title):
	#if True:
		print file_path
		content = child.find('content').text.encode('utf-8')
		content = get_content(content, link)
		macros.write_page(channel, name, file_path, title, link, content)
	index_page += '#### [' + title + '](' + file_path + ') \n'


index_file = open('../indexes/' + channel + '.md', 'w')
index_file.write(index_page)
index_file.close()

