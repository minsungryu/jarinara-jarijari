# -*- coding: utf-8 -*-

import os
import random
from dotenv import load_dotenv, find_dotenv
from slacker import Slacker

def shuffleTeams():
    teams = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(teams)

    return teams

def printSeats(teams):
    buffer = '''
    ======= 스크린 =======

    ==3==  ==2==  ==1==
       {2}조        {1}조       {0}조

    ==6==  ==5==  ==4==
       {5}조        {4}조       {3}조

    ==8==  ==7==
       {7}조        {6}조
    '''
    
    return buffer.format(*teams)

load_dotenv(find_dotenv())
token = os.getenv('SLACK_BOT_TOKEN')
slack = Slacker(token)
slack.chat.post_message(channel="#general", text=printSeats(shuffleTeams()), as_user=True)
