# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver

import time
from abc import ABC, abstractmethod
from urllib import request


class BaseBot(ABC):
    """Base class for defining Bots that scrape newspaper web pages."""

    @abstractmethod
    def get_source_url(self):
        """Returns url that will be used to fetch the data."""
        pass

    @abstractmethod
    def get_source_name(self):
        """Returns name of the newspaper."""
        pass

    @abstractmethod
    def fetch(self):
        """Makes request to source's url to fetch data."""
        pass

    @abstractmethod
    def parse(self):
        """Parses the result of the 'fetch' command into a list of JSON data."""
        pass


class EmolBot(BaseBot):
    """Bot that reads and parses news from EMOL."""

    def get_source_name(self):  # noqa
        return "EL Mercurio"

    def get_source_url(self):  # noqa
        return "http://www.emol.com/noticias/"

    def fetch(self):
        driver = webdriver.PhantomJS()
        driver.get(self.get_source_url())
        time.sleep(5)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, "html.parser")

        return soup

    def parse(self):
        soup = self.fetch()
        lis = soup.find(id='listNews').find_all('li')

        parsed_data = []

        for li in lis:
            _time = li.find(class_="bus_txt_fuente").string
            category = li.find(id="linkSeccion").string
            bajada = li.find(id="BajadaNoticia").string
            link = li.find(id="LinkNoticia")
            parsed_data.append({
                "time": _time,
                "category": category,
                "bajada": bajada,
                "url": link["href"],
                "title": link.string
            })
        return parsed_data
