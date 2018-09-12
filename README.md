Uses Requests and Beautiful Soup to scrape the /roster/ pages of mailman lists. Specifically designed only for King's College London but this can be easily changed by altering the "URL" parameter to be any mailman server you like.
Works by generating a Log In cookie for the list admin page, and then passing that cookie to the server to get the roster page. It then does a simple scrape for all the ```<a>``` tags on the page, discarding the last 4 which are admin links. 

Will immediately stop working if King's change anything to do with how the mailman server works 