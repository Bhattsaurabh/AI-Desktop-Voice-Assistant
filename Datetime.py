import datetime
from say import say


def Date():
    strfdate = datetime.datetime.today().strftime('%Y-%m-%d')
    say(f"Sir the date is {strfdate}")

def Time():
    strftime = datetime.datetime.now().strftime("%H:%M:%S")
    say(f"Sir the time is {strftime}")