# -*- coding: utf-8 -*-
from django.utils import timezone

import time
from abc import ABC, abstractmethod, abstractclassmethod

from bs4 import BeautifulSoup
from selenium import webdriver

from .models import ArticleLink


class BaseBot(ABC):
    """Base class for defining Bots that scrape newspaper web pages."""

    soup = None

    def __init__(self, soup):
        self.soup = soup

    @abstractclassmethod
    def get_source_url(cls):
        """Returns url that will be used to fetch the data."""
        pass

    @abstractmethod
    def get_source_name(self):
        """Returns name of the newspaper."""
        pass

    @abstractclassmethod
    def fetch(cls):
        """Makes request to source's url to fetch data."""
        pass

    @abstractmethod
    def parse(self):
        """Parses the result of the 'fetch' command into a list of JSON data."""
        pass


class EmolBot(BaseBot):
    """Bot that reads and parses news from EMOL."""

    def get_source_name(self):  # noqa
        return "El Mercurio"

    @classmethod
    def get_source_url(cls):  # noqa
        return "http://www.emol.com/noticias/"

    @classmethod
    def fetch(cls):
        driver = webdriver.PhantomJS()
        driver.get(cls.get_source_url())
        time.sleep(5)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, "html.parser")

        return cls(soup=soup)

    def parse(self):
        lis = self.soup.find(id='listNews').find_all('li')

        parsed_data = []

        for li in lis:
            _time = li.find(class_="bus_txt_fuente").string[:5]
            # TODO properly extract date from source!
            _date = timezone.now().today().date()
            category = li.find(id="linkSeccion").string
            bajada = li.find(id="BajadaNoticia").string
            link = li.find(id="LinkNoticia")
            parsed_data.append(
                ArticleLink(
                    headline=link.string,
                    subhead=bajada,
                    category=category,
                    time=_time,
                    url=link["href"],
                    source=self.get_source_name(),
                    date=_date
                )
            )
        return parsed_data
