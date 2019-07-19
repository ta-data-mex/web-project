![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Scraping the Brazilian Chamber of Deputies

## Overview

In this project, I practice the acquired web scraping skills going through public data about the Social Security reform proposed by the government.  
 
The main objective of the project is to obtain the voting information on all of the deliberating sessions about this constitutional amendment project until July 12th 2019, as well as to structure a system of relational databases that allows to explain basic information about the votings, such as date, specific topic of the voting and which parties are government and which are opposition. 

---

## Project Steps

This project was comprised of the following steps:

* Initial scraping of the main page dedicated to the PEC (Constitutional Amendment Project, by its acronym in Portuguese), searching for links to all the deliberating meetings (both Special Commission and House), as well as the summary of those meetings.
    * [Link to the main PEC page](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2192459)
* Scraping of each of the deliberating meetings, searching for links to the voting pages, as well as further information
* Scraping of each voting page twice:
    * Some deliberating meetings voted in more than one matter, so we may have different voting IDs with different listings. The first scrape was to obtain the voting ID and title;
    * After that, a second scrape was done to obtain the actual votes per Deputy Member. We obtained name, party and vote (Yes, No or Obstruction) to each of voters.
* Data wrangling and variable transformation.

## Future Improvements

* Pipelining the code by constructing an object to scrape the government webpage, that could be used in future projects of the same nature.
* Analysis and Data Visualization of the data obtained.

## Deliverables

* Data:
    * mother_page.csv - meeting ID, date, name, summary and link to meetings page
    * deliberacoes.csv - meeting ID, theme, address, begin (date, time), end(date, time), status, link to voting page
    * votacoes_geral.csv = voting ID, meeting ID, Title of Voting
    * votos.csv - voting ID, Deputee Name, Deputee Party, Vote
* Code:
    * mother_page_scraping.py
    * deliberating_home_scraping.py
    * vote_home_scraping.py
    * individual_vote_scraping.py