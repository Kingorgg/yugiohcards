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

import csv
import json
import requests

data = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php').json()

with open('yugioh_cards.csv', 'w', newline='', encoding='utf8') as csv_file:
    fieldnames = ['name', 'type', 'set_name', 'set_code', 'set_rarity']
    csvwriter = csv.DictWriter(csv_file, fieldnames)

    csvwriter.writeheader()
    for row in data['data']:
        if 'card_sets' in row:
            sets_data = row['card_sets']
            for sets in sets_data:
                csvwriter.writerow(
                    {
                        'name': row['name'],
                        'type': row['type'],
                        'set_name': sets['set_name'],
                        'set_code': sets['set_code'],
                        'set_rarity': sets['set_rarity'] + " " + sets['set_rarity_code']
                    }
                )
        else:
            csvwriter.writerow(
                    {
                        'name': row['name'],
                        'type': row['type'],
                        'set_name': None,
                        'set_code': None,
                        'set_rarity': None
                    }
                )

    csv_file.close()