# -*- coding: utf-8 -*-

import os
import random
from dotenv import load_dotenv, find_dotenv
from slacker import Slacker

def generateRandomSeats():
    teams = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(teams)

    seats = ''
    for desk, team in enumerate(teams):
        seats += '%d번 자리 => %d 조\n' % (desk + 1, team)

    return seats

load_dotenv(find_dotenv())
token = os.getenv('SLACK_BOT_TOKEN')
slack = Slacker(token)
slack.chat.post_message(channel="#general", text=generateRandomSeats(), as_user=True)