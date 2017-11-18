import urllib2
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0"}

def getSoup(url):
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html, "lxml")
	return soup

year = 2015

start = "http://www.cvedetails.com/vulnerability-list.php?vendor_id=452&product_id=3264&version_id=&page="
end = "&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=2016&month=0&cweid=0&order=1&trc=133&sha=df2a17fae46105e1e429e84004c3427d4c9404f5"

#http://www.cvedetails.com/vulnerability-list.php?vendor_id=452&product_id=3264&version_id=&page=2&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=2010&month=0&cweid=0&order=1&trc=107&sha=ecb1dec9e615e69ae2935fe61923ae1ed8a8df4f
numOfPages = 4

count = 0
for i in range(numOfPages):
	#url = "http://www.cvedetails.com/vulnerability-list/vendor_id-452/product_id-3264/year-2011/Mozilla-Firefox.html"
	url = start+str(i+1)+end
	soup = getSoup(url)
	bugs = soup.find_all(href=re.compile("CVE"))
	for bug in bugs:
		soup2 = getSoup("http://www.cvedetails.com"+bug['href'])
		table = soup2.find("table",attrs={"id": "vulnprodstable"})
		trs = table.find_all("tr")
		res = []
		for i in range(1,len(trs)):
			tds = trs[i].find_all("td")
			if tds[3].text.strip() == "Firefox":
				res.append(tds[4].text.strip())
		if len(res) > 0:
			print bug['href'] + " " + res[0] + " " + res[-1]
		count = count + 1
print "Total entries: ", count

#http://www.cvedetails.com/vulnerability-list.php?vendor_id=452&product_id=3264&version_id=&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=2011&month=0&cweid=0&order=1&trc=101&sha=d9aa39669b6fe27522c8a332f17894f05cf3b238
#http://www.cvedetails.com/vulnerability-list.php?vendor_id=452&product_id=3264&version_id=&page=3&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=2011&month=0&cweid=0&order=1&trc=101&sha=d9aa39669b6fe27522c8a332f17894f05cf3b238