import requests
import bs4
from bs4 import BeautifulSoup


class WebPageParser:
    def __init__(self, url):
        self.url = url
        response = requests.get(self.url)
        if response.ok:
            self.page = response
        else:
            print("Could not reach the page {1}".format(url))

    def get_text_by_tag(self, tag):
        if self.page:
            soup = BeautifulSoup(self.page.text, 'html.parser')
            tags = soup.find_all(tag)
            tag_text_arr = list()
            for tag in tags:
                if isinstance(tag.string, bs4.element.NavigableString):
                    tag_text_arr.append(tag.string.strip())
        return tag_text_arr


parser = WebPageParser("https://www.nytimes.com/")
print(parser.get_text_by_tag("h3"))


