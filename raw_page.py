import requests
from bs4 import BeautifulSoup
from url_error import UrlError


class RawPage:
    def __init__(self, url):
        self.url = url
        self._data = None
        self._headline = None

    @property
    def data(self):
        if self._data is None:
            self.__download_content()

        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def headline(self):
        if self._headline is None:
            self.__download_content()

        return self.headline

    @headline.setter
    def headline(self, new_headline):
        self._headline = new_headline

    def __download_content(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            bs = BeautifulSoup(response.text, "html.parser")
            self._headline = bs.find(class_="mw-page-title-main").text
            self._data = bs.find(class_="mw-body-content").text

        else:
            raise UrlError(self.url)
