# -*- coding: utf-8 -*-

import os
import random
from dotenv import load_dotenv, find_dotenv
from slacker import Slacker
from SeatGenerator import SeatGenerator

def shuffleTeams():
    teams = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(teams)

    return teams

def printSeats(teams):
    team_chars = ["　", "１", "２", "３", "４", "５", "６", "７", "８"]
    buffer = '''
━━━🖥━━🖥━━🖥━━━

┏━┓\t┏━┓\t┏━┓\t┏━┓
┃{0}┃\t┃{1}┃\t┃{2}┃\t┃{3}┃
┃━┃\t┃━┃\t┃━┃\t┃━┃
┃{4}┃\t┃{5}┃\t┃{6}┃\t┃{7}┃
┗━┛\t┗━┛\t┗━┛\t┗━┛

'''
    
    return buffer.format(*[team_chars[y] for x in teams for y in x])


sg = SeatGenerator(8, 7, 4)

load_dotenv(find_dotenv())
token = os.getenv('SLACK_BOT_TOKEN')
slack = Slacker(token)
slack.chat.post_message(channel="#general", text=printSeats(sg.shuffleSeats()), as_user=True)
