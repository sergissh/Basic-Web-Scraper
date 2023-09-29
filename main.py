import pandas as pd
from botScraper import scrap
from botCrawler import crawl
import time as time
def main():
    init = time.time()
    dataframe_columns = ['Title', 'Author', 'Price']
    dataframe = pd.DataFrame(columns = dataframe_columns)
    base_url = "https://www.casadellibro.com"
    visited = []
    urls = []
    #Crawler bot: Recollects urls from the web
    #bot_crawler = crawl(base_url, start_anchor)
    crawl(base_url, base_url, visited, 2, urls)
    textfile = open("urls.txt", "w")
    for element in urls:
        textfile.write(element + "\n")
    textfile.close()
    #Scraper bot: Access the URLs otained by the crawler to get the data
    #dataframe = scrap(urls, dataframe)
    dataframe = scrap(urls, dataframe)

    #Export the Dataframe to a .csv file
    dataframe.to_csv('books_data.csv', index=False)
    end = time.time()
    print(f"Scraping Time: {end-init}, for {len(urls)} URLs.")
if __name__ == "__main__":
    main()