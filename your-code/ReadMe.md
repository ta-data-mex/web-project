# Project API and Web Scraping 

## Overview 

The general objective of this proyect was to consume an API and scrap a web page and obtain a data frame that could be manipulated
later for data análisis. 

### API 

#### Overview
The API that I selected is an API from the goverment of Mexico: https://api.datos.gob.mx/v2/ It was troublesome to find, make request, and find the documentation, but finally I found a library that let you connect to a version of it.

1. First I look for an API that I could use that was related to me and where I live. I think I took to long deciding which API to use, consuming a lot of time that I could've use working. 
2. After I chose the API of aire quality of México's goverment. I had to look in various catalogs and data set for the information. The documentation was informative in some ways but others there was no clarity to what you could do or request. So it was all about trial and error. 
3. I found to endpoint from which I could request information the first one was very cryptic but had information from this year. The second one had the documentation written and was the one I use, but it only had data from last year. 
4. I made the requests to the second endpoint. From this endpoint I obtained Mexico City's data for particles 2.5. The data set occupied more than 20 pages with five thousand entries each page. 
5. I downloaded this information in json files. 
6. I opened and transform this files into pandas Data frames so I could concatenate them in one whole set. 
7. Once I made this new set with all the infomation of the files  I saved it into a csv file, so I could use this data set for other analysis. 

#### Lessons Learned

1. Don't take to long to decide which API to search or more generally speakin, don't take to long to decide on what to work. 
2. Documentation is very important to understand how to work with API's. So if an API has documentation better to read it. 
3. In retrospective I could now made the request to the other endpoint obtaining actualize data, but I couldn't do that if I hadn't learn how to make the request to the second one. 


### Web Scraper

#### Overview

For the web page scraper I chose: http://www.starcitygames.com/, this page contain information on the prices of card of a TCG call Magic the Gathering. The general purpose of this scraping was to obtain the prices of all the cards froma all sets. There are more than 65 sets each one containign approximately 250 cards. 

1. First of all I entered the page where the sets are contained and inspected it. 
2. I made requested the html page so I could use the links that link to each set. 
3. I obtained the links to each set easily. 
4. I inspected the first page of a set to see how I could obtained the information of each card and the price. This was where things got hard. All the page was constructed as a table with tables, so the information I needed was almost impossible to get using the Beautifull Soup selector function. I tried for at least four hours to retrieve the information this way. At last after getting some help I used a pandas function to read a html page. Finally it worked. 
5. After obtaining the table with the cards information and price I cleaned the data frame so it made sense and the data was ready cor use. This was properly the parser. I obtained a csv from this. 
6. Next I retrieve with an other parser the link that took you to the next page of the set. Each set had at least five pages. So the general idea was to enter the link of each set that takes you to the first page of the cards set, retrieve the table with the cards information parse, get the link to the next page, go to the next page and retrieve the table, and so on until the set was finish and then go to the next set. 
7. I tried to make this function work but, alas, I couldn't do it.  

#### Lessons Learnded

1. I understan know the pain of scraping a page built only with table of tables. Please don't do that if you are web designer. 
2. Sometimes there are other ways to obtain the information you want. Use other and look for other tools, but most importantly ask for help. 







