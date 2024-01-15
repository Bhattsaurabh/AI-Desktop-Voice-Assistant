import openai
from config import apikey
from say import say
import os




def ai(prompt):
    openai.api_key = apikey

    text = f"OpenAI response for prompt: {prompt} \n *******************\n\n"

    openai.api_key = apikey
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    #print("Jarvis :" + completion.choices[0].message["content"])
    text += completion.choices[0].message["content"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w", encoding="utf-8") as f:
        f.write(text)

    say("Output generated and saved in a Open AI folder sir...")