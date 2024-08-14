import time
from datetime import datetime

timestamp = time.strftime("%H:%M:%S")
#print(timestamp)

name= input("Enter your name: ")
#print(name,timestamp)

def rubaab() :
    hour=datetime.now().hour
    if hour>=0 and hour<12 :
        print(f"Good Morning Sir, {name}! ")
    elif hour>=12 and hour<18 :
        print(f"Good Afternoon Sir, {name}! ")
    else :
        (f"Good Evening, {name}! ")

rubaab()
   