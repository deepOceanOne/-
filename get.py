import os
import sys
import urllib2
import urllib
import requests
import re
import random
from lxml import etree
import urlparse





for filename in range(130601,130631):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

for filename in range(130701,130731):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

for filename in range(130801,130831):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

for filename in range(130901,130931):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	


for filename in range(131001,131031):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

for filename in range(131101,131131):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

for filename in range(131201,131231):
	host = "http://miniature-calendar.com/"
	#filename = "140101"
	url = host+str(filename)

	myPage = requests.get(url).content
	myPageResults =  re.findall(r'<div class="post-body">.*?<img src="(.*?)" alt.*?/>', myPage, re.S)
	news = []
	for url in myPageResults:
	    print url 	

