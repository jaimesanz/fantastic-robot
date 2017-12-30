# -*- coding: utf-8 -*-
from django.db import models


class ArticleLink(models.Model):
    """Link to an article on a newspaper website."""
    headline = models.TextField()
    subhead = models.TextField()
    category = models.CharField(max_length=128)
    time = models.TimeField()
    date = models.DateField()
    url = models.URLField()
    source = models.CharField(max_length=128)

    def __str__(self):  # noqa
        return "{} - {} - {}".format(self.source, self.date, self.time)
