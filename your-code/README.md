# Web Scraping and API consumption
## (By Daniel Herández Mota)

---
### The idea
The idea that I came up was to do an analysis of the forest fires in the last year of the "Bosque de la primavera" in Jalisco, near Guadalajara. (Sad news: This is a recurring event yearly).

![Bosque de la primavera](https://geology.com/world-cities/guadalajara-mexico.jpg)


#### Some information:

According to the National System of Forest information, the leading cause of fires is because of human action, generating 90% of the cases. These fires are usually large and devastating, affecting not only the ecosystems but the resources. It is actually a problem that accounts for many economic and ecologic loss. 

One year ago, I developed an idea to approach this problem; however, it was only theoretically proposed. I didn't had data to work on, therefore, I though that a good project could be to obtain the information with these new skills that I learned, to develop further the project.

![fire in bosque de la primavera](https://www.elsoldemexico.com.mx/republica/sociedad/2zk60h-incendio-jalisco-agapito-espinoza.jpg/alternates/LANDSCAPE_640/incendio%20jalisco%20Agapito%20Espinoza.jpg)

(Data is needed to solve any problem)


---
### The approach
What I wanted to achieve was really simple, I already had in mind the information that I needed to obtain, therefore I looked excatly for that in different databases.

I only focused in two sets of information:
- **Historical forest fire information**
- **Meteorological information** (meteorological information is imperative to determine the cause, direction and strenght of the forest fire)

The sources of information were:

1. [Datos Jalisco web page](https://datos.jalisco.gob.mx/search/type/dataset?query=incendio&sort_by=changed) for the historical forest fires.

2. [Dark Sky API](https://darksky.net/dev) for the meteorological info.

In a nutshell, Dark Sky API needs the latitude, longitude and date in order to obtain the information, this was contained in the Datos Jalisco Web Page.

---
### The code 
#### General
Code was implemented in a Jupyter Notebook where the data scraping was done first in order to obtain key information, and use that in the API. 

#### A detailed explanation
The libraries request, pandas, html5lib were imported, also BeautifulSoup and json_normalize fron bs4 and pandas.io.json respectively. 

Firstly, the WebScrapping was done.
The items that had the text 'Incendios forestales en Bosque La Primavera' also had a link that redirect to another page that had the information. 

I took all the information regarding the previous text and obtain their respective link. 

After this link was obtained, it was used to obtain other link that had the CSV files on them. I read the files with the same comand of requests.get().content. 

At this point the data of all pages was in raw form in a mixture of CSV and HTML format (this due to BeautifulSoup), this was stored in a list. A Small clean was done so that all the data had the same number of rows, and then they were converted into pandas dataframes. They were joined and exported as csv file named 'fire_data.csv'.

After this was done, the data cleaning was done: Some columns were renamed,  Unnecessary columns were droped, a check for null values was done, a description of the dataset was done, some numerical data was changed. 

The most important information was carefully manipulated: latitude, longitude and date because they had different formats. Latittude and longitude were as text in the GMS notation, GD was needed. Date was a string of dd/mm/yy, the value of Unix time was needed.

After doing this, the data was cleaned, some insights were determined and it was exported to a csv called 'fire_data_clean.csv'

After this, the values of longitude, latitude and date were used in the API (to access the API a key was needed, therefore a registration was imperative and only 1000 requests per day could be done for free.).

The request to the API was done for all the forest fires in the other dataframe. They were approximately 205 requests done. This generated a json file with the metereological data, however they had different information and therefore different lenghts, so they couldn't be that easily merged.  
Ergo, to make easier the data manipulation, all the columns were compared to see which columns were the same for all the values. In total 29 columns were used.

With this, it was possible to generate a datafeame with all the data. It was then exported to a file named 'metereological.csv'. 

However it was not clean. To clean this data, null values were changed, a refresh value was done, and the relevant information was preserved. The clean data was exported to a file named 'meteorological_clean.csv'.

At the end this both datasets were concatenated into a bigger dataframe with all the wanted information. This was saved in a final CSV file named 'forest_fire_jalisco_data.csv'.
