

# scrape
import requests
from bs4 import BeautifulSoup
import csv
r = requests.get ('https://www.census.gov/programs-surveys/popest.html')
html= (r.text)
soup = BeautifulSoup (html, 'html.parser')
search_results = soup.find_all('a')
print ("Number of URLs before processing:")
print(len(search_results))   #gets count of links
    
#parse html
unique = set()  
for link in search_results: 
    hrefs=str(link.get("href"))
    if hrefs.startswith('None'):
        ' '
    elif hrefs.startswith('#http'):
        unique.add(hrefs [1:])
        ' '
    elif hrefs.startswith ('#'):
        ' '
    elif hrefs.startswith ('/'):
        unique.add ('https://www.census.gov' + hrefs)
    elif hrefs. endswith('.gov'):
        unique.add (hrefs + '/')
    else:
        unique.add (hrefs)
    
#Output data
f= open('MyExport.csv' , 'w')
writer= csv.writer (f, delimiter =' ', lineterminator='/r')
number_lines= 0 #Initalizes the counter script
csvoutput= []
for s in unique:
    csvoutput.append(s)
    if not csvoutput:
        ' '
    else:
        writer.writerow(csvoutput)
    
    
# removes duplicates
my_list = csvoutput [0:-1]

def remove_duplicates (my_list):
	return list(set(my_list))


 
