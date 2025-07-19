from openai import OpenAI
from dotenv import load_dotenv
import os




load_dotenv()

#Version 01 Withot Memory
client=OpenAI(
    api_key=os.getenv("API_KEY"),
    #base_url=os.getenv("BASE_URL")
)
def CreateResponse(userprompt):
    response= client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":userprompt}]
     )
    return response.choices[0].message.content