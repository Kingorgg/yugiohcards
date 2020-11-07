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
import urllib.parse

from xml.etree import ElementTree
from .ygo_urls import YGOURLs

class YGOPro:
    ''' Python API Wrapper for YGOProDeck '''
    def __init__(self, response_format='json'):
        self.format = response_format
        self.url = YGOURLs()

    def __to_format(self, response):
        if self.format == 'json':
            return response.json()
        else:
            return ElementTree.fromstring(response.content)

    def __get_data(self, url):
        return self.__to_format(requests.get(url))

    def __get_image(self, url):
        return url

    def get_cards(self, **kwargs):
        '''
            The following is a list of examples you can do using the possible endpoint parameters.

            Get all cards:
            `get_cards()`

            Get "Dark Magician" card information:
            `get_cards(name='Dark Magician')`
            
            Get all cards belonging to "Blue-Eyes" archetype:
            `get_cards(archetype='Blue-Eyes')`

            Get all Level 4/RANK 4 Water cards and order by atk:
            `get_cards(level='4', attribute='water', sort='atk')`

            Get all cards on the TCG Banlist who are level 4 and order them by name (A-Z):
            `get_cards(banlist='tcg', level='4', sort='name')`

            Get all Dark attribute monsters from the Metal Raiders set:
            `get_cards(cardset='Metal Raiders', attribute='dark')`

            Get all cards with "Wizard" in their name who are LIGHT attribute monsters with a race of Spellcaster:
            `get_cards(fname='Wizard', attribute='light', race='spellcaster')`

            Get all Spell Cards that are Equip Spell Cards
            `get_cards(type='spell card', race='equip')`

            Get all Speed Duel Format Cards
            `get_cards(format='Speed Duel')`

            Get all Rush Duel Format Cards
            `get_cards(format='Rush Duel')`

            Get all Water Link Monsters who have Link Markers of "Top" and "Right"
            `get_cards(attribute='water', type='Link Monster', linkmarker='top,bottom')`

            Get Card Information while also using the misc parameter
            `get_cards(name='Tornado Dragon', misc='yes')`
        '''
        if kwargs.__len__() != 0:
            args = {}

            args.update(kwargs)

            url = self.url.card_url()+'?{args}'.format(args=urllib.parse.urlencode(args))

            return self.__get_data(url)
        else: 
            return self.__get_data(self.url.card_url())
        

    def get_random_card(self):
        ''' Returns a random card. '''
        return self.__get_data(self.url.random_card_url())

    def get_card_set_info(self, setcode=''):
        ''' Returns returns the following information:
        - `id` 
        - `name` 
        - `set_name` 
        - `set_code` 
        - `set_rarity` 
        - `set_price (in $)`
        
        based on the setcode provided. '''
        url = self.url.cards_set_info_url()
        
        if setcode != '':
            url += '?setcode={setcode}'.format(setcode=setcode)

        return self.__get_data(url)

    def get_all_card_archetypes(self):
        ''' Returns all card archetypes. '''
        return self.__get_data(self.url.all_card_archetypes_url())

    def get_database_version(self):
        ''' Returns the database version. '''
        return self.__get_data(self.url.check_db_version_url())

    def get_card_image(self, id):
        ''' Returns the url for a card image, based on the id provided. '''
        return self.__get_image(self.url.get_card_image_url().format(id=str(id)))

    def get_card_image_small(self, id):
        ''' Returns the url for a small card image, based on the id provided. '''
        return self.__get_image(self.url.get_card_image_small_url().format(id=str(id)))