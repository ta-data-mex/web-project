# Web Scrapper and API data extraction
<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

*[by Francisco Ponce]*

## Project Content


```
Web-Project
    ├── README.md
    ├── Project_2_Web_Scrapping.ipynb
    ├── Project_2_API.ipynb
    └── data
         ├── car_sales_kavak.csv
         └── sneakers.csv
 ```

### Web Scrapper: Kavak Marketplace

I'm interested to know details of the cars that are sold in the [Kavak's](https://www.kavak.com/mx/compra-de-autos) marketplace. I extracted the following data from the grid:

- Model
- Year
- Place
- Kilometers (mileage)
- Price

The pattern I followed was the pagination on params queries of the url `https://www.kavak.com/mx/page-pattern/compra-de-autos`, therefore the general information of 360 cars were outputed in a csv file for further analysis. The outputed file will be created on a **data** folder with the name **cars_marketplace_kavak**.

### Web Scrapper: Sneakers API

As a sneakers lover I'm looking forward to know the latest trends on sneakers. In order to succeed it, [the Sneakers API](https://the-sneaker-database.p.rapidapi.com/sneakers) became more than handy. 

To run our yeezy script, you need to get a [Rapid-Key](https://rapidapi.com/hub) so we can test the script. Another con is that our petitions are limited by a mothly fee so use them wisely!

#### Example
```
 headers = {
	"X-RapidAPI-Host": "the-sneaker-database.p.rapidapi.com",
	"X-RapidAPI-Key": "your key"
    }

    base_url = 'https://the-sneaker-database.p.rapidapi.com/sneakers?limit=100&page=%s'
```
    
Once we add our keys, you only need to run the script and wait for the data extraction, in order to handle the maximun number of logs per request, each response will be of 100 sneakers logs. Finally, the file will be automatically generated in a **data** folder with the name **sneakers.csv**.