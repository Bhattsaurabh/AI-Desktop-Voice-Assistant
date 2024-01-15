from say import say
from takeCommand import takeCommand



def remember():
    say("What should I remember")
    data = takeCommand()
    say("You said me to remember that" + data)
    print("You said me to remember that " + str(data))
    remember = open("data.txt", "w")
    remember.write(data)
    remember.close()


def whatremember():
    remember = open("data.txt", "r")
    say("You told me to remember that" + remember.read())
    print("You told me to remember that " + str(remember))