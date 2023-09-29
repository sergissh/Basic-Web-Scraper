import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path

books_matching = r'\d{13}'

def crawl(base_url, url, visited, depth_limit, final_urls):
    if depth_limit == 0 or len(final_urls) >=200: 
        return
    
    visited.append(url)

    try:
        response = requests.get(url + '/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            links = soup.find_all('a', href=True)
            for link in links:
                next_url = link['href']
                if len(next_url) < 120 and next_url.startswith('/') and len(next_url) > 0:
                    next_url = base_url + next_url
                    if next_url not in visited:
                        if re.search(books_matching, next_url) and next_url not in final_urls:
                            final_urls.append(next_url)
                            print("Added")
                        else:
                            crawl(base_url, next_url, visited, depth_limit - 1, final_urls)

                        
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")
