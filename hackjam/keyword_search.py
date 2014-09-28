import mechanize
import cookielib
import urllib
import urlparse
import urllib2
import codecs
from bs4 import BeautifulSoup

def key_word_search_result(keyWord, num_result=10):
	filename = keyWord

	br = mechanize.Browser()
	br.set_handle_robots(False)
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query=' + urllib2.quote('"' + filename + '"') + '&d=PTXT'
	htmltext = urllib2.urlopen(url).read()
	soup = BeautifulSoup(htmltext)
	raw_info = []
	
	for t in soup.findAll('tr'):
		for tr in t.findAll('td', {'valign': "top"}):
			raw_info += tr
	# key: number from 1 to num_result
	# value = (PAT NO, Discription)
	dictionary = {}
	for i in range(num_result):
		lable = int(str(raw_info[i*3].string).replace(",", ""))
		number = int(str(raw_info[i*3+1].string).replace(",", ""))
		div = str(raw_info[i*3 + 2].string).replace(",", "")[:-1]
		dictionary[lable] = (number, div)
	return dictionary



