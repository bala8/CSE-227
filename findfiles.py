import urllib.request
from bs4 import BeautifulSoup
import re
import csv

import sys

base_url =  "https://www.openhub.net/p/firefox/commits?query=1167489&time_span=48+months"	#raw_input('Enter - ')
for id in range(959531, 959532):
	url = "https://www.openhub.net/p/firefox/commits?query="+str(id)+"&time_span=48+months"
	html = urllib.request.urlopen(url).read()

	soup = BeautifulSoup(html, "lxml")

	#print (soup.prettify()[-10000:-1].encode(sys.stdout.encoding, errors='replace'))	#print last 10k lines, replace unknown characters with '?'				
	
	# Retrieve all of the anchor tags
	tags = soup('a')

	span_fields = soup('span')
	#div_fields = soup('div')
	print(url)
	#print(tags)
	for tag in tags:
		link = tag.get('href', None)
		#print(link)
		if link!=[] and link!=None:
			commit = re.findall("commits/[0-9]", link)
			if commit!=[]:
				print("https://www.openhub.net/"+link)
				new_url = "https://www.openhub.net/"+link
				
				req = urllib.request.Request(new_url, headers={'User-Agent': 'Mozilla/5.0'})	#Specify User-Agent here to download complete page
				html = urllib.request.urlopen(req).read()
				#html = urllib.request.urlopen(url).read()
				
				soup = BeautifulSoup(html, "lxml")
				#tables = soup.findAll("table")
				
				#rows = soup.findAll('td', {'class': 'strong'})
				#print(rows)
				list = ["File","Language","Code Added","Code Removed","Comments Added","Comments Removed","Blanks Added","Blanks Removed"]
				code_diff = [0, 0]
				
				print("\nby Language")
				i=0
				rows = soup.findAll('tr', {'class': 'odd'})
				if rows!=[]:
					for row in rows:
						all_td = row.find_all('td')
						for td in all_td:
							if i==1:
								print(list[i],td.contents[0])
							if i==2 or i==3:
								code_diff[i-2] = code_diff[i-2]+int(td.contents[0])
								print(list[i],td.contents[0],"Total",code_diff[i-2])
							i=i+1
						print("\n")
				
				i=0
				rows = soup.findAll('tr', {'class': 'even'})
				if rows!=[]:
					for row in rows:
						all_td = row.find_all('td')
						for td in all_td:
							if i==1:
								print(list[i],td.contents[0])
							if i==2 or i==3:
								code_diff[i-2] = code_diff[i-2]+int(td.contents[0])
								print(list[i],td.contents[0],"Total",code_diff[i-2])
							i=i+1
						print("\n")
				
				print("\nby File")
				i=0
				rows = soup.findAll('tr', {'class': 'odd nohover'})
				if rows!=[]:
					for row in rows:
						all_td = row.find_all('td')
						for td in all_td:
							if i==0 or i==1:
								print(list[i],td.contents[0])
							if i==2 or i==3:
								#code_diff[i-2] = code_diff[i-2]+int(td.contents[0])
								print(list[i],td.contents[0])
							i=i+1
						print("\n")
				
				i=0
				rows = soup.findAll('tr', {'class': 'even nohover'})
				if rows!=[]:
					for row in rows:
						all_td = row.find_all('td')
						for td in all_td:
							if i==0 or i==1:
								print(list[i],td.contents[0])
							if i==2 or i==3:
								#code_diff[i-2] = code_diff[i-2]+int(td.contents[0])
								print(list[i],td.contents[0])
							i=i+1
						print("\n")
						
				

	if(id%100==0):
		print(id)