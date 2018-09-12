#  Mailman Downloader

Uses Requests and Beautiful Soup to scrape the ```/roster/``` pages of [mailman]http://www.list.org/) lists. Specifically designed only for [King's College London](https://mailman.kcl.ac.uk) but this can be easily changed by altering the "URL" parameter to be any mailman server you like.

Works by generating a log-in cookie for the list admin page, and then passing that cookie to the server to get the roster page. It then does a simple scrape for all the ```<a>``` tags on the page, discarding the last 4 which are admin links on King's mailman sites. 

Will probably immediately stop working if King's change anything to do with how the mailman server works. 

## 3rd Party Module Requirements
* [Requests](http://docs.python-requests.org/en/master/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

