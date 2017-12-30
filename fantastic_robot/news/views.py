# -*- coding: utf-8 -*-
from django.shortcuts import render

from .bots import EmolBot


def home(request):
    emol = EmolBot.fetch()
    print(emol.parse())
    return render(request, 'news/home.html', {
        "data": emol.parse()
    })
