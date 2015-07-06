#!/usr/bin/env python
#!encoding:utf-8

from scapy.all import *
import getopt
import sys
sys.path.append('/root/Py/X/')
from core import mycolor

'''
    这是一个网络工具集，功能实现将网卡置与监听模式：
    1.抓取网络中的数据流
    2.监听Cookie获取后实现会话劫持
    3.简单的中间人欺骗
    4.隐藏的wifi嗅探
    。。。。
'''

'''定义变量'''
traffic = False
snif	= False
payload = None
probe   = []

print( mycolor.color.red + mycolor.color.bold +
	"""
	MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	MM							 MM
	MM               TheSniff  v0.9				 MM
	MM		 Coded by  kin13		         MM
	MM		 Email     2996479828@qq.com		 MM
	MM               Date      15/4/19			 MM
	MM                                                       MM
	MMMMMMMMMM				       MMMMMMMMMMMM
	MMMMMMMMMM                                     MMMMMMMMMMMM
	*********************************************************** 
	""" + mycolor.color.end)

''' 用法 '''
def usage():

    print(mycolor.color.green + "Usage thesniff.py [OPTIONS]")
    print("-t --traffic   \t\t - 监听网络IP地址")
    print("-i --inter     \t\t - 使用的网卡模式")
    print("-s --snif      \t\t - 监听web流量，配合使用-p")
    print("-p --payload   \t\t - 使用payload，查找web流量")
    print("-f --find	  \t - 侦探所用的wifi")
    print("-h --help      \t\t - help")

''' 存储数据包到文件中 '''
def save(payload,path_file):
 
    with open(path_file,'w') as f:
	f.write(payload)
	f.close()

''' 抓取网络中的IP流'''
def monitor_pkt(pkt):

    if pkt.haslayer(IP):
	if pkt.haslayer(Ether):
	    net1 = pkt.sprintf(mycolor.color.green + "[+]%IP.src%:%TCP.sport% (%Ether.src%)  " + \
		"-->  %IP.dst%:%TCP.dport% (%Ether.dst%)\t%TCP.flags%")
	    print(net1)
	else:
	    net2 = pkt.sprintf("[+]%IP.src%:%TCP.sport%  "  + \
		"-->  %IP.dst%:%TCP.dport% \t%TCP.flags%")
	    print(net2)
	
''' 抓取网络中web的请求,设置一个变量payload 来抓取Raw中的内容'''
def monitor_web(pkt):

    if pkt.haslayer(Raw):
	payloads = pkt.getlayer(Raw).load
	if payload in payloads:
	    print(pkt.sprintf("[+]%IP.src%:%TCP.sport% --> %IP.dst%:%TCP.dport% \t%TCP.flags%"))
	    print('\n' + payloads)

''' 侦探wifi'''	    
def monitor_wifi(pkt):

    if pkt.haslayer(Dot11):
	if pkt.type == 0 and pkt.subtype == 8:
	    if pkt.addr2 not in probe:
		probe.append(pkt.addr2)
		cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}{Dot11ProbeResp:%Dot11ProbeResq.cap%}")
		if re.search('privacy',cap):
		    a = '[+]加密状态:Yes\tBSSID:%s\tSSID:%s' %(pkt.addr2, pkt.info)
		    print(a)
		else:
		    b = '[+]加密状态:No\tBSSID:%s\tSSID:%s' %(pkt.addr2, pkt.info)
		    print(b)

def main():
    
    global traffic
    global snif
    global payload
    global probe
 
    if not len(sys.argv[1:]):
	usage()
 
    try:
	opts, args = getopt.getopt(sys.argv[1:],"ti:sp:hf",["traffic","inter",\
	    "snif","payload","help","find"])
    except getopt.GetoptError as err:
	print(str(err))
	exit()

    for o,a in opts:
	if o in ("-h","--help"):
	    usage()
	    exit(0)
	elif o in ("-t","--traffic"):
	    traffic = True
	elif o in ("-i","--inter"):
	    conf.iface = a
	elif o in ("-s","--sniff"):
	    snif = True
	elif o in ("-p","--payload"):
	    payload = a
	elif o in ("-f","--find"):
	    sniff(prn=monitor_wifi)
	else:
	    print("error options")
    
    if traffic == True and snif == True :
	print("[!] Using traffic or snif")
	exit() 
    if traffic:
	print("[+] Using Traffic Starting Monitor Networking on " + conf.iface)
	sniff(prn=monitor_pkt)
    if snif:
	if payload == None:
	    print("[!] Using -p to specify payload ")
	    exit(0)
	print("[+] Using Snif Starting Monitor Web on " + conf.iface)
	sniff(prn=monitor_web)

if __name__ == '__main__':
    main()
