from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re

for start in range(0,1001,10):
    try:
        url="https://www.indeed.co.in/jobs?q=engineer&l=Delhi&start={}".format(start)
        html_doc=urlopen(url).read()
        soup=BeautifulSoup(html_doc,'html.parser')
        
        #to deal with encoding error
        with open("x.html","w",encoding="utf-8") as f:
            f.write(str(soup))

        with open("x.html","r") as f:
            with open("data.csv","a") as f2:
                writer=csv.writer(f2)
                
                html=f.read()
                new_soup=BeautifulSoup(html,'html.parser')
                jobs=new_soup.findAll(class_=["jobsearch-SerpJobCard" ,"unifiedRow" ,"row","result","clickcard"])

                for job in jobs:
                    #to remove unwanted tags inbetween the text
                    [s.extract() for s in job(['style', 'script', '[document]', 'head', 'title'])]
                    
                    #no need of rating tab so we are gonna remove it too
                    ratingContent=job.find(class_="ratingsContent")
                    if ratingContent:
                        ratingContent.extract()

                    #removing unwanted newlines ,whitespaces
                    data=re.sub(r'[\r\n][\r\n]{1,}', '\n', job.text).strip().split("\n")[0:4]

                    #adding the link attribute for easy redirection
                    link="https://www.indeed.co.in/jobs?q={}&l={}".format(data[0],data[2])
                    data.append(link)

                    #appending the data in the csv file
                    writer.writerow(data)

            #status checking        
            print("page done{}".format(start))   
            
    except Exception as e:
        print(e)            