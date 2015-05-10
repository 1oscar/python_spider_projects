#/bin/env python
#coding=utf-8

import urllib
import urllib2
import re
import traceback

title_pat = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)


class Tie_ba:
    def __init__(self, base_url, only_louzhu):
        self.base_url = base_url
	self.only_louzhu = '?see_lz='+str(only_louzhu)

    def get_page(self):
	try:
	    url = self.base_url + self.only_louzhu
	    request = urllib2.Request(url)
	    response =  urllib2.urlopen(request) 
	    page = response.read()
	    
	   # f = open('tie_ba.html', 'w')
	   # f.write(page)
	    return response.read()
	    
	except Exception, e:
	    traceback.print_exc()


    def get_title(self):
	#page = self.get_page()
	with open('tie_ba.html', 'r') as f:
	    page = f.read()
	title_obj = re.search(title_pat, page)
	if title_obj:
            title =  title.group(1).strip()
	    print title
	else:
	    return None
	

	
    

if __name__ == '__main__':
    base_url = 'http://tieba.baidu.com/p/3727055946'
    only_louzhu = 1
    tie_ba = Tie_ba(base_url, only_louzhu)
    #tie_ba.get_page()
    tie_ba.get_title()

