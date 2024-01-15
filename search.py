import pywhatkit as kt
from say import say
from config import phoneno

def searchOnGoogle(data):
   data = data.split()[3:]
   say("output generated sir...")
   kt.search(data)


def sendMsg():
   try:
      # sending message to receiver
      # using pywhatkit
      kt.sendwhatmsg(phoneno, "Hello from GeeksforGeeks", 00, 53)
      print("Successfully Sent!")

   except:

      # handling exception
      # and printing error message
      print("An Unexpected Error!")