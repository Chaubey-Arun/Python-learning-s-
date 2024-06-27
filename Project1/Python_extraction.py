import json
import requests
from bs4 import BeautifulSoup
file = open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json','r')
x =file.read ()
web_url= json.loads(x)
m = web_url['url']
for links in m :
    print('\nlink-',links) 


