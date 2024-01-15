
import openai
from say import say
from config import apikey

chatStr = " "

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Saurabh: {query} Jarvis: "
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    print("Jarvis :" + completion.choices[0].message["content"])
    say(completion.choices[0].message["content"])
    chatStr += completion.choices[0].message["content"]
    return completion.choices[0].message["content"]


def resetChat():
    say("chat reset Sir...")
    chatStr = " "