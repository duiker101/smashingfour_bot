import re

import praw
import requests

from credentials import *

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent='smashingfour_bot:v1.0 (by /u/smashingfour_bot)',
                     )


def get_cards():
    url = 'https://duiker101-smashingfour-v1.p.mashape.com/cards'
    headers = {"X-Mashape-Key": mashape_key,
               "Accept": "application/json"}
    r = requests.get(url, headers=headers)
    return r.json()


def get_message_to_reply():
    for mention in reddit.inbox.mentions(limit=1):

        match = re.match(r'.+?card:([a-zA-Z]+)\b', mention.body)
        if match:
            # reddit.inbox.mark_read([mention])
            return match.groups()[0], mention
    return None, None


card_name, message = get_message_to_reply()
if card_name:
    cards = get_cards()
    for card in cards:
        if card_name.lower() in card['name'].lower():
            # print(card)
            comment = (
                    '**%s**\n\n' % card['name'] +
                    'Ability: %s\n\n' % card['ability'] +
                    'Rarity: %s\n\n' % card['rarity']['name'] +
                    'Speed: %s\n\n' % card['speed']['name'] +
                    'Weight: %s\n\n' % card['weight']['name'] +
                    'Size: %s\n\n' % card['size']['name'] +
                    '|Level|Attack|Health|Ability|\n' +
                    '|:-|:-|:-|:-|\n'
            )

            for level in card['levels']:
                lvl = level['level']
                hp = level['hp']
                dmg = level['dmg']
                ab = level['ability'] if level['ability'] > 0 else '' + ''
                comment = comment + '|%d|%d|%d|%s|\n' % (lvl, hp, dmg, ab)

            reddit.comment(message).reply(comment)
            break
