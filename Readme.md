# Building a basic Web Scraper

## Step-by-step guide to creating a basic Web Scraper

<b>Web Scraping</b> refers to the automated process of extracting data from web pages using software tools or scripts. Typically, the goal is to compile a dataset, conduct analysis or to performe research.
In this repository I have crafted a straightforward <b>Python</b> script that leverages the Selenium and BeautyfulSoup libraries to gather book-related information from the "La Casa del Libro" website. 
</br>
To build this bot Web Scraper, it's essential to delineate its core components:
1. Web Crawling: This phase involves the retrieval of pertinent URLs of interest.
2. HTML Parsing: Here, we dissect the HTML structure of these pages and extract their content.
3. Data Extraction: The final step entails extracting the specific data of interest from the HTML code.

This project exemplifies the seamless integration of these components to facilitate data retrieval and analysis.


Data: 3552 seconds for 235 URLs that leaves us with a mean of 15,1 seconds for page visited and data extracted

## Dependencies
The Packages we have used are:
- Pandas: 
- Selenium
- Requests
- BeautifulSoup

## Getting Started
### Installation
To ensure the successful installation of this project and its dependencies, it is essential to have both <b>Git</b> and <b>pip</b> already installed.
</br></br>
Clone this repository:
```bash
git clone https://github.com/sergissh/Basic-Web-Scraper.git
cd Basic-Web-Scraper
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
The project is now ready to use!

### Usage
Execute the scraper:
```bash
python main.py
```
