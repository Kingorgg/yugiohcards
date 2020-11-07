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

class URLs:
    ''' URL Class that has all the endpoints for the YGOProDeck API.'''
    def __init__(self):
        self.base_url = 'https://db.ygoprodeck.com/api/v7/'

        # All card info
        self.all_cards = 'cardinfo.php'

        # Random card
        self.random_card = 'randomcard.php'

        # Card set info
        self.cards_set_info = 'cardsetsinfo.php'

        # All Card Archetypes
        self.all_card_archetypes = 'archetypes.php'

        # Check DB Version
        self.check_db_version = 'checkDBVer.php'

    def base_url(self):
        ''' Return Base URL. '''
        return self.base_url

    def all_cards_url(self):
        ''' Return All Cards URL. '''
        return self.base_url + self.all_cards
    
    def random_card_url(self):
        ''' Return Random Card URL. '''
        return self.base_url + self.random_card

    def cards_set_info_url(self):
        ''' Return Card Set Info URL. '''
        return self.base_url + self.card_set_info

    def all_card_archetypes_url(self):
        ''' Return All Card Archetypes URL. '''
        return self.base_url + self.all_card_archetypes

    def check_db_version_url(self):
        ''' Return Check DB Version URL. '''
        return self.base_url + self.check_db_version