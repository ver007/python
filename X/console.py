#!/usr/bin/env python
#!encoding:utf

from core import mycolor
from core import header
from core import menu,help
import os
from modules import dirbb

def main():

    try:
	line = mycolor.color.blue + mycolor.color.underl + 'ksf' + mycolor.color.end
	line += ' > '
	terminal = raw_input(line)
	if terminal == 'banner':
	    header.main_header()
	    menu.main_info()
	    main()
	elif terminal == 'exit':
	    exit(0)
	elif terminal == 'help':
	    help.help()
	    main()
	elif terminal[0:2] == 'os':
	    os.system(terminal[3:])
	    main()
	elif terminal[0:3] == 'use':
	    if terminal[4:20] == 'web/dir_scan':
		dirbb.dirscan()
		main()

	else:
	    print("wrong command!using help")
	    main()
    except KeyboardInterrupt:
	print("[*]Tring to exit...")

header.main_header()
menu.main_info()
main()
