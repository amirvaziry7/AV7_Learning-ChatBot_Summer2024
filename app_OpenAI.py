from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
import requests


load_dotenv()

#Version 01 Withot Memory
client=OpenAI(
    api_key=os.getenv("API_KEY"),
    #base_url=os.getenv("BASE_URL")
)

# while True:
#     user_prompt=input("Please Write Your Question :")
#     response= client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role":"user","content":user_prompt}]
#     )
#     #print(response)
#     print(response.choices[0].message.content)


#version 02 WithMemory

# messages=[
#     {"role":"system","content":"You are Helpfull Asissant"}
# ]

# while True:
#     user_prompt=input("Please Write Your Question :")
#     messages.append(
#         {"role":"user","content":user_prompt}
#     )
#     response=client.chat.completions.create(
#         model="gpt-4",
#         messages=messages
#     )
#     print(response.choices[0].message.content)
#     messages.append(
#         {"role":"assistant","content":response.choices[0].message.content}
#     )



#version 03 WithMemory and Change Temp

# messages=[
#     {"role":"system","content":"You are Helpfull Asissant"}
# ]

# while True:
#     user_prompt=input("Please Write Your Question :")
#     messages.append(
#         {"role":"user","content":user_prompt}
#     )
#     response=client.chat.completions.create(
#         model="gpt-4",
#         messages=messages,
#         temperature=1
#     )
#     print(response.choices[0].message.content)
#     messages.append(
#         {"role":"assistant","content":response.choices[0].message.content}
#     )


#version 04 Generate Image With gpt-image-1

# while True:
#     user_prompt=input("Please Enter Your Prompt:")
#     response= chat.images.generate(
#         model="gpt-image-1",
#         n=1,
#         prompt=user_prompt,
#         size="1024x1024"
#     )
#     print(response.data[0])
#     img_byte=base64.b64decode(response.data[0].b64_json)
#     with open("output.png","wb") as f:
#         f.write(img_byte)

#version 04 Generate Image With DAL-e

# while True:
#     user_prompt=input("Please Enter Your Prompt:")
#     response= client.images.generate(
#         model="dall-e-3",
#         n=1,
#         prompt=user_prompt,
#         size="1024x1024"
#     )
#     response_download = requests.get(response.data[0].url)

#     if response_download.status_code == 200:
#         with open("Img/image.png", "wb") as f:
#             f.write(response_download.content)
#         print("✅ Image downloaded successfully.")
#     else:
#         print(f"❌ Failed to download. Status code: {response.status_code}")