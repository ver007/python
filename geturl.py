#!/usr/bin/env python
#!encoding:utf-8

'''
    这只是一个分析网页源码的小程序
    只使用-u 遍历目标地址链接，只到二级链接为止
    加上-a 加 -t 使用另一个模式，得到目标url的标签
			    by   kin13
			    qq   2996415828
			    data 15/5/5
'''

from bs4 import BeautifulSoup
import requests
import Queue
from urlparse import urlsplit
import optparse

def get_url(url):

    url_list = []

    r    = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text)
    
    for link in soup.find_all('a'):
	try:
	    new_url = urlsplit(link['href'])[1]
	except:pass

	if new_url not in url_list and url not in url_list:
	    url_list.append(new_url)

    print("[+] ---> " + url)
    for x in url_list:print('\t' + x)
    return url_list

def url_all(url,tag):

    r    = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text)
    for t in soup.find_all(tag):
	print(t.prettify())

def main():

    parser = optparse.OptionParser("Usage:%prog -u <url> | -a <url_all> -t <tag>")
    
    parser.add_option('-u','--url',dest='url',type='string',\
	help='Specify target url')
    parser.add_option('-a','--all',dest='all',\
	action='store_true',default=False,help='Show verbose url')
    parser.add_option('-t','--tag',dest='tag',type='string',\
	help='Specify tag for url')

    (options,args) = parser.parse_args()

    if options.url == None:
	print(parser.usage)
	exit(0)

    if options.all:
	if options.tag == None:
	    print("[-]Using tag")
	    exit()
	else:
	    print("[+] Get all tag for " + options.url)
	    url_all(options.url,options.tag)
	    exit(0)

    url_queue = Queue.Queue()
    for q in get_url(options.url):
	url_queue.put(q)

    while not url_queue.empty():
	new_link = 'http://' + url_queue.get()
	try:
	    get_url(new_link)
	except:pass

if __name__ == '__main__':

    main()
