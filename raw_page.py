import requests
from bs4 import BeautifulSoup
from url_error import UrlError


class RawPage:
    """Represents a raw web page and provides methods for downloading its content."""

    def __init__(self, url):
        """Initialize RawPage with the given URL.

        Args:
            url (str): The URL of the web page.
        """
        self.url = url
        self._data = None
        self._headline = None

    @property
    def data(self):
        """Property method to get the raw data of the web page.

        Returns:
            str: The raw data of the web page.
        """
        if self._data is None:
            self.__download_content()

        return self._data

    @data.setter
    def data(self, new_data):
        """Setter method to set the raw data of the web page.

        Args:
            new_data (str): The new raw data to set.
        """
        self._data = new_data

    @property
    def headline(self):
        """Property method to get the headline of the web page.

        Returns:
            str: The headline of the web page.
        """
        if self._headline is None:
            self.__download_content()

        return self._headline

    @headline.setter
    def headline(self, new_headline):
        """Setter method to set the headline of the web page.

        Args:
            new_headline (str): The new headline to set.
        """
        self._headline = new_headline

    def __download_content(self):
        """Private method to download the content of the web page using requests and BeautifulSoup.

        Raises:
            UrlError: If the HTTP response status code is not 200.
        """
        response = requests.get(self.url)

        if response.status_code == 200:
            bs = BeautifulSoup(response.text, "html.parser")
            self._headline = bs.find(class_="mw-page-title-main").text
            self._data = bs.find(class_="mw-body-content").text

        else:
            raise UrlError(self.url)
