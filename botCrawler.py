import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path

books_matching = r'\d{13}'
base_url = "https://www.casadellibro.com"
def crawl(url, visited, depth_limit, save_urls):
    if depth_limit == 0 or len(save_urls) >=200: 
        return
    visited.append(url)

    try:
        response = requests.get(url + '/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            links = soup.find_all('a', href=True)
            for link in links:
                
                next_url = link['href']
                if len(next_url) > 0 and len(next_url) < 120 and next_url not in visited:
                    if next_url.startswith('/'):
                        if re.search(books_matching, next_url) and base_url + next_url not in save_urls and 'libro' in next_url:
                            save_urls.append(base_url + next_url)
                        else:
                            crawl(base_url + next_url, visited, depth_limit - 1, save_urls)
                    else:
                        crawl(next_url, visited, depth_limit - 1, save_urls)
                        
    except Exception as e:
        print(f"Error crawling {next_url}: {str(e)}")
