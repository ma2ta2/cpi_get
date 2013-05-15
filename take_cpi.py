#! /Users/MK/Documents/python/test/
# -*- coding: UTF-8 -*-

import time
import datetime

#指標が増えたらファイルへ出す
def take_cpi():
	try:
		print 'take_cpi start'
		import cpi_read
		cr = cpi_read.cpi_read()
		cr.cpi_read_m()
	except:
		print 'err take_cpi'
		raise
		
if __name__=='__main__':
	try:
		today = datetime.date.today()
		print 'hiduke_check start /', today.month
		take_cpi()

	except:
		print 'exit'
		sys.exit(1)