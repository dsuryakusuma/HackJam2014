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

    # value = (PAT NO, Discription)
    dictionary = []
    for i in range(num_result):
        number = str(raw_info[i*3+1].string).replace(",", "")
        div = str(raw_info[i*3 + 2].string).replace(",", "").replace("\n", "")
        div = " ".join(div.split())
        dictionary += ((number, div),)
    return dictionary

def get_pdf(pat_num):
    filename = keyWord

    br = mechanize.Browser()
    br.set_handle_robots(False)
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=1&r=1&f=G&l=1&d=PTXT&s1='+str(pat_num)+'.PN.'
    
    url2 = 'http://pdfpiw.uspto.gov/.piw?Docid=0'+str(pat_num) +'&homeurl=http%3A%2F%2Fpatft.uspto.gov%2Fnetacgi%2Fnph-Parser%3FSect1%3DPTO2%2526Sect2%3DHITOFF%2526u%3D%25252Fnetahtml%25252FPTO%25252Fsearch-adv.htm%2526r%3D1%2526p%3D1%2526f%3DG%2526l%3D50%2526d%3DPTXT%2526S1%3D%252522slide%252Bunlock%252522%2526OS%3D%252522slide%252Bto%252Bunlock%252522%2526RS%3D%252522slide%252Bto%252Bunlock%252522&PageNum=&Rtype=&SectionNum=&idkey=NONE&Input=View+first+page'

    htmltext = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmltext)

def get_par_num(pat_num):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=1&r=1&f=G&l=1&d=PTXT&s1='+ urllib2.quote(pat_num) +'.PN.'
    
    htmltext = urllib2.urlopen(url).read()
    soup = BeautifulSoup(htmltext)

    raw_info = []
    for t in soup.findAll('tr'):
        for tr in t.findAll('td', {'align': "left"}):
            raw_info += tr
    raw_info = [str(t.string) for t in raw_info if len(str(t.string)) > 4 and str(t.string)[0].isdigit()]
    return raw_info