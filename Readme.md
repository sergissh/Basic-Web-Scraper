# Building a basic Web Scraper

## Step-by-step guide to creating a basic Web Scraper

<b>Web Scraping</b> refers to the automated process of extracting data from web pages using software tools or scripts. Typically, the goal is to compile a dataset, conduct analysis or to performe research.
In this repository I have crafted a straightforward <b>Python</b> script that leverages the Selenium and BeautyfulSoup libraries to gather book-related information from the "La Casa del Libro" website. 
</br>
To build this bot Web Scraper, it's essential to delineate its core components:
1. <b>Web Crawling:</b> This phase involves the retrieval of pertinent URLs of interest.
2. <b>HTML Parsing:</b> Here, we dissect the HTML structure of these pages and extract their content.
3. <b>Data Extraction:</b> The final step entails extracting the specific data of interest from the HTML code.

This project exemplifies the seamless integration of these components to facilitate data retrieval and analysis.


Data: 3552 seconds for 235 URLs that leaves us with a mean of 15,1 seconds for page visited and data extracted

## Dependencies
The Packages we have used are:
- Pandas==2.0.1
- Selenium==4.13.0
- Requests==2.27.1
- BeautifulSoup==4.11.1

## Web Crawling
The initial step to create a scraper bot is to collect all the URLs from which we intend to gather information. To acomplish this, we'll develop a Crawler bot that will automatically retrieve these URLs for us. </br>
A web crawling , in essence, acts as a digital cartographer, mapping the intrincate network of routes and URLs within a website. It systematically records these paths, therefore enabling the acces of each one by the scraper bot for the data extraction.
</br>
</br>
### DFS - Search Algorithm

Para poder recorrer todo el árbol de rutas de la web utilizaremos el algoritmo de búsqueda DFS (Depth First Search), el cual recorre el árbol de rutas de forma completa explotando cada camino hasta su nodo hoja.

```python
    #Pseudo-code of the DFS algorithm
    def dfs(url, visited):
        #Add current URL to the visited list
        visited.append(url)

        #HTTP Request of the URL to retrieve the HTML content
        response = requests.get(url)
        if response.status_code == 200:
            
            #Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            #Find all the links in the HTML
            links = soup.find_all('a', href=True)

            #Iterate each link
            for link in links:

                #Extract href attribute of a tag
                next_url = link['href']
                if next_url not in visited:

                    #Recursive call
                    crawl(next_url, visited)
                        
```
En este pseudo-código tenemos la estructura base del algoritmo DFS para nuestro bot crawler, el qual es una <a href="https://www.campusmvp.es/recursos/post/Que-es-la-recursividad-o-recursion-Un-ejemplo-con-JavaScript.aspx"><b>Función Recursiva</b></a> que permite obtener todos los links de la web y explorar las ramas de forma profunda. Para obtener el contenido HTML de la URL primero tenemos que realizar una petición GET HTTP con la libreria Requests, y posteriormente inicializar un objeto de BeautyfulSoup para poder acceder a su contenido de forma sencilla.

### Pattern Matching
Para poder crear un web scraper es muy importante analizar los patrones dentro de la página web a explotar, siendo este factor también importante para el bot crawler. En nuestro caso no queremos todas las rutas de la web sinó solo aquellas que contengan datos de libros, por lo que si solo nos quedamos con esas URLs nos ahorarremos visitar las que no sean de interés. 
<div align="center">
    <img width="80%" src="./images/URL-pattern.png" />
</div>
En nuestro caso hemos detectado que las URLs que contienen datos de libros siempre contienen una especie de identificador de 13 números, por lo que podemos utilizar un pattern matching sobre las URLs a guardar.

```python
    #This patter matching requires to have 13 numbers inside the string/URL
    books_matching = r'\d{13}'

    #Extract href attribute of a tag
    next_url = link['href']
    if next_url not in visited:
        # Apply the pattern matching and store the URL
        if re.search(books_matching, next_url) and next_url not in save_urls:
            save_urls.append(next_url)
```

### Bot Crawler Considerations

Por tal de agilizar este programa y no obtener miles y miles de URLs a scrapear (ya que como veremos más adelante no es un proceso rápido) hemos limitado el número máximo de URLs a recoger. Esto lo hemos hecho de la siguiente manera:

- Limitando a 200 el número de URLs a guardar.
- Limitando la profundidad a la que explorar el árbol de URLs, en nuestro caso a 2. 

Se puede jugar con estos dos parámetros pero hay que tener en cuenta que cuando más profundicemos en el árbol, y cuantas más URLs guardemos más tardará la ejecución del bot crawler.





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
