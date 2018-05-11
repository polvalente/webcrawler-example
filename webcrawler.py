import urllib
from bs4 import BeautifulSoup
import re
from sys import argv

class WebCrawler(object):
    def __init__(self):
        pass

    def crawl(self, url):
        if "http" not in url:
            url = "http://"+url
        
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html5lib")
        data = soup.findAll(text=True)
        
        def visible(element):
            if element.parent.name in ["style", "script", "[document]", "head", "title"]:
                return False
            elif re.match('<!--.*-->', str(element.encode('utf-8'))):
                return False
            elif re.match('\s', str(element.encode('utf-8'))):
                return False
            return True


        text = [element for element in data if visible(element)]
        text = [element.lstrip().rstrip() for element in text]
        text = [element for element in text if (len(element) > 0)]

        frequencies = {}
        for item in text:
            if item not in frequencies:
                frequencies[item] = 0
            frequencies[item] += 1
        
        return frequencies

if __name__ == "__main__":
    url = "" if len(argv) <= 1 else argv[1]
    app = WebCrawler()
    print(app.crawl(url))
