
import os

#We need a list of date string in the date range we want.
from datetime import datetime, timedelta

start_date = "2018-08-01"
stop_date = "2018-12-31"

start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

dates = list()
while start <= stop:
    dates.append(start.strftime('%Y%m%d'))
    start = start + timedelta(days=1)



import requests
from bs4 import BeautifulSoup as bs



#Now write a function to parse the HTML response, return the data we want(title, content, ...etc).
def process_document(document):
    
    nodes = document.select('ul.list > li')
    data = list()
    

    for li in nodes:

        # check if is empty element
        if li.select_one('a') == None:
            continue

        # get link
        li_link = 'http://news.ltn.com.tw/' + li.select_one('a')['href']

        # request for document
        li_res = requests.get(li_link)
        li_doc = bs(li_res.text, 'lxml')

        #get title
        li_title = li.select_one('p').get_text()

        #get content
        li_content = ""
        for ele in li_doc.select('div.text > p'):
            if not 'appE1121' in ele.get('class', []):
                li_content += ele.get_text()

        # append new row
        data.append({       
            'title': li_title,          
            'content' : li_content,
        })
    return data



#Crawl over the news on the site, store the data in variable "all_data" .
cnt = 0
all_data = list()
for date in dates:
    print('start crawling :', date)
    res = requests.get('https://news.ltn.com.tw/list/newspaper/life/' + date)
    doc = bs(res.text, 'lxml')
    data = process_document(doc)
    all_data += data
    
    


#Save as pkl file
import pickle

with open('life_crawler.pkl', 'wb') as f:
    pickle.dump(all_data, f)    



#Turn it into pandas dataframe(二維表格)
import pandas as pd
pd.DataFrame(all_data)[[ 'title', 'content']].head() #head預設為前5rows






