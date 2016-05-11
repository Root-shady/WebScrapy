# WebScrapy
The following tools are required:
  python2.7  scrapy 1.0.6 
  
(1). To use the MySQLStorePipeline, you need to install MySQLDB
Update the following code in settings.py:
```python
  MYSQL_HOST = 'localhost'
  MYSQL_DBNAME = 'webScrape'
  MYSQL_USER = 'root'
  MYSQL_PASSWD = 'password'
```
Use the following command to start the scraper:
  $ scrapy crawl uniqlo
  
