import feedparser
from concurrent.futures import ThreadPoolExecutor

# List of feeds
feeds = ['https://gizmodo.com/rss',
         'https://engadget.com/rss.xml',
         'https://feeds.arstechnica.com/arstechnica/index']

# Function to extract titles from single feed
def get_titles(feed):
    titles = []
    
    entries = feedparser.parse(feed).entries
    for entry in entries: 
        titles.append(entry.title)
        
    return titles

all_titles = []

# Parallel execution  
with ThreadPoolExecutor() as executor:
    
    # Map feeds to function 
    results = executor.map(get_titles, feeds)
    
    # Concatenate results
    for result in results:
        all_titles.extend(result)
        
print(f"Total titles: {len(all_titles)}")
        
with open('titles.txt','w') as f:
    f.write('\n'.join(all_titles))
    
print('Done writing titles!')