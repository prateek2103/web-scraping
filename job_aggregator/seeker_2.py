from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re

urls=[{"url_name":"indeed","url":"https://www.indeed.co.in/jobs?q={}&l={}","class_tag":"div","class":"jobsearch-SerpJobCard unifiedRow row result clickcard","encoding":True},
      {"url_name":"linkedin","url":"https://in.linkedin.com/jobs/search?keywords={}&location={}","class_tag":"li","class":"result-card job-result-card result-card--with-hover-state","encoding":False}]

f1="engineer";f2="Delhi"


for url in urls:
    print(url["url_name"]+" jobs:")
    html_doc=urlopen(url["url"].format(f1,f2)).read()
    soup=BeautifulSoup(html_doc,'html.parser')
            
    #to deal with encoding error
    if(url['encoding']==True):
        with open("x.html","w",encoding="utf-8") as f:
          f.write(str(soup))

        with open("x.html","r") as f:
            new_html=f.read()
            new_soup=BeautifulSoup(new_html,"html.parser")
            soup=new_soup        
        
    blocks=soup.find_all(url["class_tag"],class_=url["class"].split(' '))
    #print(blocks)

    for block in blocks:
        #print(block)
        title=block.select_one("[class*=title]")
        company=block.select_one("[class*=subtitle]") or block.select_one("[class*=company]")
        location=block.select_one("[class*=location]")
        salary=block.select_one("[class*=salary]")
        link=block.select_one("a")['href']
        if(url["url_name"] not in link):
            link="https://www."+url["url_name"]+".com"+link
        
        print(link)
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        if not salary == None:
            print(salary.text.strip())
            
        print('\n')