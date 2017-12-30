# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class BaseBot(ABC):
    """Base class for defining Bots that scrape newspaper web pages."""

    @abstractmethod
    def get_source_url(self):
        pass

    @abstractmethod
    def get_source_name(self):
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def parse(self):
        pass


class EmolBot(BaseBot):
    """Bot that reads and parses news from EMOL."""

    pass
