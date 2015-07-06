#!/usr/bin/env python

import requests
from threading import Thread
import Queue
import sys
from core import mycolor
from core import help

options = ["http://www.bilibili.com","/root/Py/X/dir.txt",30]
tag = mycolor.color.blue + mycolor.color.bold + "[+]" + mycolor.color.end

def dirscan():

    line_1 = mycolor.color.blue + mycolor.color.underl + "ksf" + mycolor.color.end
    line_1 += ':'
    line_1 += mycolor.color.blue + mycolor.color.underl + "Dir Scan" + mycolor.color.end
    line_1 += ' > ' 

    com = raw_input(line_1)

    if com[0:10] == 'set THREAD':
	threads = com[11:]
	options[2] = threads
	print(tag + "set threads --> " + str(options[2]))
	dirscan()

    elif com[0:9] == 'set RHOST':
	target = com[10:]
	options[0] = target
	print(tag + "set RHOST --> " + options[0])
	dirscan()
    
    elif com[0:8] == 'set FILE':
	file_path = com[9:30]
	options[1] = file_path
	print(tag + 'set FILE --> ' + options[1])
	dirscan()

    elif com[0:12] == 'show options':
	print("")
	print("Options\t\t Value\t\t\t Description")
	print("-------\t\t---------------------\t-----------------")
	print("RHOST\t\t"  + options[0] + "\t Target url")
	print("FILE\t\t"   + options[1] + "\tFile path")
	print("THREAD\t\t" + str(options[2]) + "\t\t\t Specify Threads")
	dirscan()

    elif com[0:2] == 'os':
	os.system(com[3:])
	dirscan()

    elif com[0:4] == 'help':
	help.help()
	dirscan()
    
    elif com[0:4] == 'back':
	pass
    
    elif com[0:3] == 'run':
	print(mycolor.color.bold + mycolor.color.blue + "[*] Scan url" + mycolor.color.end)	
	dir_path = Queue.Queue()
	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/10100101 Firefox/19.0'}

	with open(options[1],'r') as f:
	    for line in f.readlines():
		if not line.startswith('#'):
		    line = line.rstrip()
		    dir_path.put(line)
	    f.close()
	
	def scan(url):		
	    while not dir_path.empty():
		if url[-1:] != '/':
		    url += '/'

		url += dir_path.get()
		r = requests.get(url,headers=headers)
		if r.status_code == 200:
		    code = mycolor.color.red + '200' + mycolor.color.end
		elif r.status_code == 403:
		    code = mycolor.color.yellow + '403' + mycolor.color.end
		else:
		    code = mycolor.color.blue + str(r.status_code) + mycolor.color.end
	
		if r.status_code != 404:
		    print(tag + mycolor.color.green + r.url + '\t' + mycolor.color.end + code)
		url = options[0]
	    
	for t in range(options[2]):
	    Thread(target=scan,args=(options[0],)).start()

    else:
	dirscan()
