from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
        html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
        bsObj = BeautifulSoup(html)
        nameList=bsObj.findAll("span",{"class":"green"})
        nameList = bsObj.findAll("span", {"class":"green"})
        for name in nameList:
                 print(name.get_text())
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It Worked!")
