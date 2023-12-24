import requests
import pytz
from datetime import datetime
import time
import os
from io import TextIOWrapper

YEAR = 2023
MAX_DAY = 25

session = str(os.environ.get('AOC_SESSION'))
cookies = {'session': session}

def updateData(day = None):
    current_time = datetime.now(pytz.timezone('US/Eastern'))

    if current_time.year < YEAR:
        print(f"It's not time yet! Wait for {YEAR}.")
        return
    
    if current_time.month < 12 and current_time.year == YEAR:
        print("It's not time yet! Wait for December.")
        return
    
    if current_time.month == 12 and current_time.year == YEAR:
        max_day = min(current_time.day, MAX_DAY)
    else:
        max_day = MAX_DAY
    
    if day is None:
        for day in range(1, max_day+1):
            getDay(day)
    else:
        if day < max_day+1:
            getDay(day)

def getDay(day):
    if not os.path.isfile(f'data/{day}.txt'):
        r = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', cookies=cookies)
        
        f = open(f'data/{day}.txt', 'w')
        f.write(r.text)
        f.close()
    
    if not os.path.isfile(f'data/test{day}.txt'):
        f = open(f'data/test{day}.txt', 'w')
        f.write("")
        f.close()

def loadDay(day, test=False, tryUpdateData=True):
    filepath = f"./data/test{day}.txt" if test else f"./data/{day}.txt"
    return open(filepath)