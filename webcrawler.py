import urllib
from bs4 import BeautifulSoup
import re

class WebCrawler(object):
    def __init__(self):
        pass

    def crawl(self, url):
        if "http" not in url:
            url = "http://"+url
        
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html)
        data = soup.findAll(text=True)
        
        def visible(element):
            if element.parent.name in ["style", "script", "[document]", "head", "title"]:
                return False
            elif re.match('<!--.*-->', str(element.encode('utf-8'))):
                return False
            return True

        text = [element for element in data if visible(element)]
        frequencies = {}
        for item in text:
            if item not in frequencies:
                frequencies[item] = 0
            frequencies[item] += 1

        sorted_freqs = sorted(list(frequencies.items()), key=lambda x: x[1])
        words, frequencies = zip(*sorted_freqs)

        return words, frequencies
