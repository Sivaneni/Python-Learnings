import feedparser
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from itertools import chain

# List of feeds
feeds = ['https://gizmodo.com/rss',
         'https://engadget.com/rss.xml',
         'https://feeds.arstechnica.com/arstechnica/index']

# Function to extract links from single feed
def get_titles(feed):
    titles = []
    
    entries = feedparser.parse(feed).entries
    for entry in entries: 
        titles.append(entry.link)

    #print(titles)
        
    return titles

all_titles = []

#function to extract content from each link
def getcontent(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)  

    soup = BeautifulSoup(resp.content, 'html.parser')

    # Get article title
    title = soup.find('h1').text
    
    title=f'Title:  {title} \n\n'

    # Get content 
    main = soup.find('div', class_=['js_post-content','caas-content','content-wrapper'])
    if main:

        para_text = [p.get_text() for p in main.find_all('p')]
        article_content = " ".join(para_text)
    else:
        article_content='NO js_post-content class to pull paragrapghs'
    #print(type(title+article_content))
    return str(title+article_content)

# Parallel execution write all contents from feed urls and there title to a file
with open('content.txt','w',encoding='utf-8') as f:

    with ThreadPoolExecutor() as executor:
    
    # Map feeds to function 
        urls = list(executor.map(get_titles, feeds))
        flatten_urls=list(chain(*urls))
       
        results=executor.map(getcontent, flatten_urls)
 
    
    # Concatenate results
        for result in list(results):
      
            f.write(str(result))
            f.write('\n\n\n\n')
    
        


    
print('Done writing content and titles to content file from all 121 links from above 3 feeds !')