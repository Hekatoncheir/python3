from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

basehtml = "http://www.mzitu.com/18"





liststemp = bs1.find("div", {"class": "pagenavi"}).findAll("a")
lists.add(liststemp[len(liststemp)-1].attrs["href"])