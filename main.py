
import os
import time
import webbrowser

from say import say
from search import searchOnGoogle, sendMsg
from chat import  resetChat, chat
from takeCommand import takeCommand
from mail import sendMail
from ai import ai
from weather import weatherReport
from news import newsReport
from Datetime import Date, Time
from remember import remember, whatremember
from Stop import stop


def action():
    print('Pycharm')
    say("Hello I am Saurabh's assistant. my name is Jarvis")
    while True:
        print("Listening...")
        query = takeCommand()

        #todo: for websites
        sites = [["gmail", "https://mail.google.com/mail/u/0/#inbox"], ["youtube", "https://youtube.com"],["Graphic Era Hill University Website", "https://www.gehu.ac.in/"], ["Graphic Era Hill University ERP", "https://student.gehu.ac.in/Account/Cyborg_StudentMenu"]]

        for site in sites:
            if f" {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir...")
                webbrowser.open(site[1])

        #todo: for system file/folders
        lists = [["play music", "D:\my music\Make You Mine.mp3"], ["music list", "D:\my music"], ["song", "D:\my music\Make You Mine.mp3"] ]

        if "open".lower() or "play".lower() in query.lower():
            for list in lists:
                if f"{list[0]}".lower() in query.lower():
                    say(f"opening {list[0]} sir...")
                    os.startfile(list[1])


        #todo: for system apps
        apps = [["camera", "start microsoft.windows.camera:"], ["calculator", "calc"], ["notepad", "notepad"]]

        if "open".lower() in query.lower():
            for app in apps:
                if f"{app[0]}".lower() in query.lower():
                    say(f"opening {app[0]} sir...")
                    os.system(app[1])


        # todo : for killing processes
        #processes = [["camera", "taskkill /im WindowsCamera.exe /f"], ["google tabs", "taskkill /im chrome.exe /f"], ["file explorer", "taskkill /im explorer.exe /f "], ["music", "taskkill /im vlc.exe"]]

        #if "close".lower() in query.lower():
        #    for process in processes:
        #        if f"{process[0]}".lower() in query.lower():
        #            say(f"closing {process[0]} sir...")
        #            os.system(process[1])


        #todo: for closing browser windows


        #todo: for google search

        if "search on google".lower() in query.lower():
            searchOnGoogle(query)

        if "send message".lower() in query.lower():
            sendMsg()

        #todo: for system commands
        commands = [["shutdown", "shutdown /s"], ["restart", "shutdown /r"], ["log of", "shutdown /l"]]

        for command in commands:
            if f"{command[0]}".lower() in query.lower():
                say(f"{command[0]} the system sir...")
                os.system(command[1])



        #todo: for sending emails
        emailids = [["Saurabh", "@gmail.com"],["rohit", "@gmail.com"],["Saurav", "@gmail.com"], ["rishabh", "@gmail.com"], ["Aastha", "@gmail.com"]]

        if "send a mail to" in query:
            for name in emailids:
                if f"{name[0]}".lower() in query.lower():
                    try:

                        say("say what you want to send in mail")
                        time.sleep(3)
                        say("say now sir...")
                        content = takeCommand()
                        print(content+"\n")
                        sendMail(name[1], content)
                        say("email successfully sended sir...")
                    except Exception as e:
                        print(e)
                        say("Sorry sir I am not able to send this email right now please try again")


        elif "the time" in query.lower():
            Time()
        elif "the date" in query.lower():
            Date()

        elif "vs code" in query:
            path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            say("opening vs code sir")
            os.startfile(path)

        elif "reset chat".lower() in query.lower():
            resetChat()

        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "chatting".lower() in query.lower():
            say("chatting started Sir...")
            #query = takeCommand()
            while True:
                print("chatting")
                query = takeCommand()
                if "stop chatting".lower() in query.lower():
                    say("chat stopped Sir...")
                    break
                chat(query)

        elif "show weather report" in query.lower():
            say("tell me the place sir...")
            location = takeCommand()
            weatherReport(location)

        elif "show news report" in query.lower():
            newsReport("in")

        elif "remember that" in query:
            remember()

        elif "do you remember anything" in query:
            whatremember()

        elif "stop working" in query.lower():
            stop()


        #else:  say("Sorry sir I am not able to understand your query please try again")
"""
if __name__ == '__main__':
    action()
"""
