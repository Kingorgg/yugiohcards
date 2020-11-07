# -*- coding: utf-8 -*-

'''
MIT License

Copyright (c) 2020 Daniel Taylor (kingorgg)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Data Source provided by https://db.ygoprodeck.com/api-guide/
'''

import json
import requests

from xml.etree import ElementTree
from urls import *

class YGOProDeckAPI:
    ''' Python API Wrapper for YGOProDeck '''
    def __init__(self, response_format='json'):
        self.format = response_format
        self.url = URLs()

    def __to_format(self, response):
        if self.format == 'json':
            return response.json()
        else:
            return ElementTree.fromstring(response.content)

    def __get_data(self, url):
        return self.__to_format(requests.get(url))

    def get_cards(self):
        return self.__get_data(self.url.all_cards_url())

    def get_random_card(self):
        return self.__get_data(self.url.random_card_url())

    def get_card_set_info(self):
        return self.__get_data(self.url.cards_set_info_url())

    def get_all_card_archetypes(self):
        return self.__get_data(self.url.all_card_archetypes_url())

    def get_database_version(self):
        return self.__get_data(self.url.check_db_version_url())