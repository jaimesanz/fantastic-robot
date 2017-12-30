# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


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
        print("wena")
        return "asf"

    def parse(self):
        return "sdf"
