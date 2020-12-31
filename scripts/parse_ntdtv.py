#!/usr/bin/python
# coding: utf-8

import macros
import sys
import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

channel = sys.argv[1]
channel_url = sys.argv[2]

index_page = '' + macros.head
links = macros.tail


def get_content(url):
	response = requests.get(url)
	text = response.text.encode('utf-8').replace('</p>\n</p>','</p>')
	parser = BeautifulSoup(text, 'html.parser')
	for img in parser.find_all('img'):
		del img['width']
		del img['height']
	for link in parser.find_all('div', attrs = {'class': 'print_link'}):
		link.decompose()
	post_title = parser.find('div', attrs = {'class': 'featured_image'})
	if post_title is None:
		post_title = ''
	else:
		try:
			post_title.find('a').unwrap()
		except:
			pass
		post_title = '<div>' + post_title.prettify().encode('utf-8') \
			.replace('</figure>','</figure><br/>') + '</div><hr/>' + macros.proxy
	post_content = parser.find('div', attrs = {'class': 'post_content'})
	if post_content is None:
		return '-'
	for related in post_content.find_all('div', attrs = {'class': 'post_related'}):
		related.decompose()
	for iframe in post_content.find_all('iframe'):
		iframe.decompose()
	post_content = '<div>' + post_content.prettify().encode('utf-8') + '</div>'
	return post_title + post_content \
		.replace('<a href', '<ok href').replace('</a>', '</ok>') \
		.replace('</figure>','</figure><br/>') \
        .replace('<figcaption','<br/><figcaption') \
        .replace('</figcaption>','</figcaption><br/>') \
        .replace('<h2>', '<h4>') \
        .replace('<h2 ', '<h4 ') \
        .replace('</h2>', '</h4>')


def get_name(link):
	fname = link.split('/')[-1]
	aid  = fname.split('.')[0]
	return aid


index_text = requests.get(channel_url).text.encode('utf-8')
index_html = BeautifulSoup(index_text, 'html.parser')
articles = index_html.find('div', attrs = {'class': 'list_wrapper'}).find_all('div', attrs = {'class': 'one_post'})
for article in articles:
	a_links = article.find_all('a')
	if len(a_links) < 2:
		continue
	link = a_links[1]
	a_url = link.get('href').encode('utf-8')
	a_title = link.text.encode('utf-8').strip()
	name = get_name(a_url) + '.md'
	file_path = '../pages/' + channel + '/' + name 
	#content = get_content(a_url)

	if not os.path.exists(file_path):
	#if True:
		print file_path
		content = get_content(a_url)
		macros.write_page(channel, name, file_path, a_title, a_url, content)
	index_page += '#### [' + a_title + '](' + file_path + ') \n'


index_file = open('../indexes/' + channel + '.md', 'w')
index_file.write(index_page)
index_file.close()



