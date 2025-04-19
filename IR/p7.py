from bs4 import  BeautifulSoup
import requests

try:
    response=requests.get("https://wikipedia.com")
    soap = BeautifulSoup(response.text,"html.parser")
    for link in soap.find_all("a",href=True):
         print(link["href"])
except Exception as e:
     print(f"Failed to crawl wikipedia: {e}")
