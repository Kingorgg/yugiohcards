# yugiohcards

For more information on the API, please visit https://db.ygoprodeck.com/api-guide/

This is intended to be an easy to use wrapper for python projects.

## Requirements
* certifi==2020.6.20
* chardet==3.0.4
* idna==2.10
* requests==2.24.0
* urllib3==1.25.11

## Example on how to use this API Wrapper

### Import YGOProDeckAPI

```python
from ygoprodeck import *
```

### Initiate YGOProDeckAPI

```python
ygo = YGOProDeckAPI()
```

### get_cards()
> **Rate Limiting** on the API is **enabled**. The rate limit is **20 requests per 1 second**. If you exceed this, you are blocked from accessing the API for 1 hour. **ygoprodeck** will monitor this rate limit for now and adjust accordingly.

#### Available Parameters
The following is a list of examples you can do using the possible endpoint parameters.

* **name** - The exact name of the card.
* **fname** - A fuzzy search using a string. For example `&fname=Magician` to search by all cards with "Magician" in the name.
* **id** - The ID of the card. You **cannot** pass this alongside name. You can pass multiple comma separated IDs to this parameter.
* **type** - The type of card you want to filter by. See below "Card Types Returned" to see all available types. You can pass multiple comma separated Types to this parameter.
* **atk** - Filter by atk value.
* **def** - Filter by def value.
* **level** - Filter by card level/RANK.
* **race** - Filter by the card race which is officially called type (Spellcaster, Warrior, Insect, etc). This is also used for Spell/Trap cards (see below). You can pass multiple comma separated Races to this parameter.
* **attribute** - Filter by the card attribute. You can pass multiple comma separated Attributes to this parameter.
* **link** - Filter the cards by Link value.
* **linkmarker** - Filter the cards by Link Marker value (Top, Bottom, Left, Right, Bottom-Left, Bottom-Right, Top-Left, Top-Right). You can pass multiple comma separated values to this parameter (see examples below).
* **scale** - Filter the cards by Pendulum Scale value.
* **cardset** - Filter the cards by card set (Metal Raiders, Soul Fusion, etc).
* **archetype** - Filter the cards by archetype (Dark Magician, Prank-Kids, Blue-Eyes, etc).
* **banlist** - Filter the cards by banlist (TCG, OCG, Goat).
* **sort** - Sort the order of the cards (atk, def, name, type, level, id, new).
* **format** - Sort the format of the cards (goat, ocg goat, speed duel, rush duel, duel links). Note: Duel Links is not 100% accurate but is close.
* **misc** - Show additional response info (Card Views, Beta Name, etc.).
* **staple** - Check if card is a staple.
* **has_effect** - Check if a card actually has an effect or not by passing a boolean true/false. Examples of cards that do not have an actual effect: Black Skull Dragon, LANphorhynchus, etc etc.

You can also use the following equation symbols for `atk`, `def` and `level`:
* **"lt"** (less than)
* **"lte"** (less than equals to)
* **"gt"** (greater than)
* **"gte"** (greater than equals to).

Examples: `atk=lt2500` (atk is less than 2500), `def=gte2000` (def is greater than or equal to 2000) and `level=lte8` (level is less than or equal to 8).

The specific results from this endpoint are cached for **2 days (172800 seconds)** but will be manually cleared upon new card entry.

#### Get all cards:
```python
ygo.get_cards()
```

#### Get "Dark Magician" card information:
```python
ygo.get_cards(name='Dark Magician')
```

#### Get all cards belonging to "Blue-Eyes" archetype:
```python
ygo.get_cards(archetype='Blue-Eyes')
```

#### Get all Level 4/RANK 4 Water cards and order by atk:
```python
ygo.get_cards(level='4', attribute='water', sort='atk')
```

#### Get all cards on the TCG Banlist who are level 4 and order them by name (A-Z):
```python
ygo.get_cards(banlist='tcg', level='4', sort='name')
```

#### Get all Dark attribute monsters from the Metal Raiders set:
```python
ygo.get_cards(cardset='Metal Raiders', attribute='dark')
```

#### Get all cards with "Wizard" in their name who are LIGHT attribute monsters with a race of Spellcaster:
```python
ygo.get_cards(fname='Wizard', attribute='light', race='spellcaster')
```

#### Get all Spell Cards that are Equip Spell Cards:
```python
ygo.get_cards(type='spell card', race='equip')
```

#### Get all Speed Duel Format Cards:
```python
ygo.get_cards(format='Speed Duel')
```

#### Get all Rush Duel Format Cards:
```python
ygo.get_cards(format='Rush Duel')
```

#### Get all Water Link Monsters who have Link Markers of "Top" and "Right":
```python
ygo.get_cards(attribute='water', type='Link Monster', linkmarker='top,bottom')
```

#### Get Card Information while also using the misc parameter:
```python
ygo.get_cards(name='Tornado Dragon', misc='yes')
```

### get_random_card()
Displays a random card.
```python
ygo.get_random_card()
```

### get_card_set_info(`setcode=''`)
> This follows the same rate limiting procedures as the card lookup endpoint.

This requires a parameter of `"setcode"`.
```python
ygo.get_card_set_info(setcode='SDY-046')
```
This returns the following information: `id`, `name`, `set_name`, `set_code`, `set_rarity` and `set_price (in $)`.

### get_all_card_archetypes()
> This follows the same rate limiting procedures as the card lookup endpoint.

This simply returns all of the current Yu-Gi-Oh! Card Archetype Names stored in the database.
```python
ygo.get_all_card_archetypes()
```
Use this to get a quick snapshot of all the Yu-Gi-Oh! Card Archtypes sorted by A-Z.

### get_database_version()
This is not a cached endpoint and database_version and date are incremented when:
* New card is added to the database.
* Card information is updated/modified on the main database.
```python
ygo.get_database_version()
```

### get_card_image(id)
Retrieves a url for a card image, based on an `id` provided. Images are in `.jpg`.
```python
ygo.get_card_image(id=27551)
```

### get_card_image_small(id)
Retrieves a url for a smaller card image, based on an `id` provided. Images are in `.jpg`.
```python
ygo.get_card_image_small(id=27551)
```