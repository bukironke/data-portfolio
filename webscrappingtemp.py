#A web scrapping exercise that has the functions - BeautifulSoup and requests which shows the price of an item 
from bs4 import BeautifulSoup
import requests 

url = "www.apple.com"
result = requests.get(url)
doc = BeautifulSoup (result.text, "html.parser")


prices = doc.find_all(text= "£")
parent = prices[0].parent 
holder = parent.find ("holder")
print(holder.string)
#Variable 'holder' symbolises the tag that the price is under, the tag varies between the design of the website
#Output may vary due to security regulation on most websites but the purpose was to show the structure behind getting the desired output.