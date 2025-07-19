# **************************************************
# pip install -U streamlit
# python -m pip install -U streamlit
#
# pip3 install -U streamlit
# python3 -m pip3 install -U streamlit
# **************************************************


# **************************************************
# python .\streamlit_app.py
# **************************************************
# import streamlit

# print("Streamlit Version:", streamlit.__version__)
# **************************************************


# **************************************************
# python .\streamlit_app.py
# **************************************************
# import os
# import streamlit

# os.system(command="cls")

# print("Streamlit Version:", streamlit.__version__)
# **************************************************


# **************************************************
# python .\streamlit_app.py
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# print("Streamlit Version:", st.__version__)
# **************************************************


# **************************************************
# Notes:
#
# 1) app.py                    --> streamlit_app.py
# 2) python ./streamlit_app.py --> streamlit run ./streamlit_app.py
# **************************************************


# **************************************************
# streamlit run ./streamlit_app.py
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.write("Hello, World!")  # <p>
# **************************************************


# **************************************************
# Note: Do Not Write Below Codes!
#
# import os
# os.system(command="cls")
# **************************************************


# **************************************************
# import streamlit as st
# import os

# os.system(command="cls")

# st.write("Hello, World!")  # <p>
# **************************************************


# **************************************************
# import streamlit as st

# st.write("Hello, World!")
# st.write("I'm Amir Vaziry!")
# **************************************************


# **************************************************
# In One Line!
# **************************************************
# import streamlit as st

# st.write("Hello, World!", "I'm Amir Vaziry!")
# **************************************************


# **************************************************
# Using Markdown
# **************************************************
# import streamlit as st

# st.header(body="Amir Vaziry")  # <h2> --> Best Practice

# st.markdown(body="## Amir Vaziry")  # <h2>

# st.markdown(body="<h2>Amir Vaziry</h2>")  # می‌کند Encode به خاطر مسائل امنیتی

# st.markdown(body="<h2>Amir Vaziry</h2>", unsafe_allow_html=True)
# st.markdown(body="`Print('Hello World')`")
# st.markdown(body="> This is Quote")
# **************************************************


# **************************************************
# import streamlit as st

# st.header(body="Sample (1)")

# st.markdown(body="# Amir Vaziry")
# st.markdown(body="## Amir Vaziry")
# st.markdown(body="### Amir Vaziry")
# st.markdown(body="#### Amir Vaziry")
# st.markdown(body="##### Amir Vaziry")
# st.markdown(body="###### Amir Vaziry")
# #st.markdown(body="---")
# st.divider()

# st.header(body="Sample (2)")

# st.write("# *Amir Vaziry*")
# st.write("## Amir Vaziry")
# st.write("### Amir Vaziry")
# st.write("#### Amir Vaziry")
# st.write("##### Amir Vaziry")
# st.write("###### Amir Vaziry")
# st.divider()

# # body = """# Amir Vaziry
# # ## Amir Vaziry
# # ### Amir Vaziry
# # #### Amir Vaziry
# # ##### Amir Vaziry
# # ###### Amir Vaziry"""

# # body = """
# # # Amir Vaziry
# # ## Amir Vaziry
# # ### Amir Vaziry
# # #### Amir Vaziry
# # ##### Amir Vaziry
# # ###### Amir Vaziry
# # """

# st.header(body="Sample (3)")

# body = """\
# # Amir Vaziry
# ## Amir Vaziry
# ### Amir Vaziry
# #### Amir Vaziry
# ##### Amir Vaziry
# ###### Amir Vaziry
# *amir vaziry*
# """

# st.markdown(body=body)
# st.divider()

# st.header(body="Sample (4)")

# st.write(body)
# st.divider()
# **************************************************


# **************************************************
# https://gitlab.com/-/snippets/2526872
# https://gist.github.com/rxaviers/7360908
# https://gohugo.io/quick-reference/emojis
# https://github.com/ikatyang/emoji-cheat-sheet
# https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
# **************************************************


# **************************************************
#import streamlit as st

# نکته مهم: این دستور باید اول نوشته شود
# st.set_page_config(page_title="Amir Vaziry", page_icon="👋")
# st.set_page_config(page_title="Amir Vaziry", page_icon="👋", layout="wide")

# st.header(body="Amir")
# st.header(body="👋 Amir")
# st.header(body=":anguished: Amir")
# st.header(body="Amir", divider="violet")
# **************************************************


# **************************************************
# import streamlit as st

# st.title(body="👋 Welcome to Amir's Streamlit App!")  # <h1>
# #st.header(body="👋 Welcome to Amir's Streamlit App!")  # <h2>
# #st.subheader(body="👋 Welcome to Amir's Streamlit App!")  # <h3>

# st.markdown(body="Hello, _Amir_! :kiss:")  # (_) --> Italic
# # st.markdown(body="Hello, **Amir**! :computer:")  # (**) --> Bold
# st.divider()

# # st.write("Hello, _Amir_! :kiss:")
# st.write("Hello, **Amir**! :computer:")
# st.divider()

# st.caption(body="This is a small text!")
# st.divider()

# st.write("[Learn More](https://IranianExperts.ir)")  # Link (Anchor)
# st.divider()

# code_example = """
# def greet(name):
#     result = f'Hello, {name}!'
#     return result
# """

# st.code(body=code_example, language="python")
# st.markdown(body=f"`{code_example}`")
# st.divider()
# **************************************************


# **************************************************
# import streamlit as st

# st.warning(body="Warning",icon="⚠️")
# st.divider()

# st.error(body="Error")
# st.divider()

# st.info(body="Info")
# st.divider()

# st.success(body="Success")
# st.divider()

# ex = RuntimeError("This is an exception of type RuntimeError")
# st.exception(exception=ex)
# st.divider()
# **************************************************


# **************************************************
# Display Image
# **************************************************
# import os
# import streamlit as st

# # آدرس‌دهی نسبی، نسبت به جایی که هستیم
# image_file_path: str = "./Img/image.png"

# st.image(image=image_file_path)
# st.image(image=image_file_path, width=200)
# st.write("Image File Path:", image_file_path)
# st.divider()

# # آدرس‌دهی فیزیکی
# # C:\Program Files\...
# image_file_path = os.path.join(os.getcwd(),  "Img", "image.png")

# st.image(image=image_file_path, width=200)
# st.write("Image File Path:", image_file_path)
# st.divider()
# **************************************************


# **************************************************
# import streamlit as st

# pressed = st.button(label="Press Me",help="if you clicked it Show This help",type="primary",use_container_width=True)

# if pressed:
#     st.warning(body="You pressed the button!",icon="🔥")
# **************************************************

# **************************************************
# Learning: toast()
# **************************************************
# import streamlit as st

# pressed = st.button(label="Press Me")

# if pressed:
#     st.toast(body="Wow! You did it...", icon="👋")

#     st.write("You pressed the button!")
# **************************************************


# **************************************************
# دو چیز باحال و هیجان‌انگیز
# **************************************************
# import streamlit as st

# button_1_pressed = st.button(label="Button (1)")

# if button_1_pressed:
#     st.snow()
#     st.write("You pressed the button (1)!")

# button_2_pressed = st.button(label="Button (2)")

# if button_2_pressed:
#     st.balloons()
#     st.write("You pressed the button (2)!")
# **************************************************


# **************************************************
import streamlit as st

# name: str = st.text_input(label="Your Name")

# #st.write(f"Hello, {name}!")
# # **************************************************


# # **************************************************
# # Python Note!
# #
# # python .\streamlit_app.py
# # **************************************************
# # import os

# # os.system(command="cls")

# # name = None
# # name = "Amir"

# if name != " " and name !="" :
#     st.info(body=f"WellCome {name}")
# elif name == "":
#     st.success(body="Write SomeThings")
# elif name==" ":
#     st.toast(body="Name is not None! and is not Null String")

# **************************************************


# **************************************************
# import streamlit as st

# name = st.text_input(label="Name")

# # if name is not None and name != "":
# #     st.write(f"Hello, {name}!")

# if name:
#     st.write(f"Hello, {name}!")
# **************************************************


# **************************************************
# یک مشکل اساسی
# **************************************************
# import streamlit as st

# number: int = 0

# pressed = st.button(label="Press Me")

# if pressed:
#     number += 1
#     st.write(f"Number: {number}")
# **************************************************


# **************************************************
# حل مشکل اساسی
# **************************************************
# import streamlit as st

# # مهم: دستور ذیل صحیح نمی‌باشد
# # st.session_state.number = 0

# # if not st.session_state.get(key="number"):
# #     st.session_state.number = 0

# # OR

# if "UserClicked" not in st.session_state:
#     st.session_state.UserClicked = 0

# pressed = st.button(label="Press Me")

# if pressed:
#     st.session_state.UserClicked += 1
#     st.write(f"You are : {st.session_state.UserClicked} Clicked")
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Create Chatbot Step by Step
# **************************************************
# import streamlit as st

# st.set_page_config(page_title="Learning Create Chatbot With ST", page_icon="👋")

# st.header(body="Learning Chatbot", divider="rainbow")
# #st.text_input(label="please Enter YourName")
# st.chat_input()

# with st.chat_message(name="USER"):  # "User" OR "Human" OR "HUMAN"
#     st.write("I want to know about your products.")

# with st.chat_message(name="AI"):
#     st.write("Hello! How can I help you?")


# **************************************************


# **************************************************
# import streamlit as st

# # New
# AI: str = "AI"
# USER: str = "USER"

# st.set_page_config(page_title="Learning Chatbot", page_icon="👋")

# # New
# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")
    

# st.header(body="DT Chatbot", divider="rainbow")

# st.chat_input(placeholder="Type your question here...")

# with st.chat_message(name=AI):
#     st.write("Hello! How can I help you?")

# with st.chat_message(name=USER):
#     st.write("I want to know about your products.")
# **************************************************


# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# # New
# user_prompt = st.chat_input(placeholder="Type your question here...")

# # New
# if user_prompt:
#     with st.chat_message(name=USER):
#         st.write(user_prompt)

#     with st.chat_message(name=AI):
#         assistant_answer: str = f"I don't know! {user_prompt}"
#         st.write(assistant_answer)
# **************************************************


# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# # New
# def Havij(user_prompt: str) -> str:
#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# # New
# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     assistant_answer: str = Havij(user_prompt=user_prompt)

#     with st.chat_message(name=USER):
#         st.write(user_prompt)

#     with st.chat_message(name=AI):
#         st.write(assistant_answer)
# **************************************************


# **************************************************
# We Need Chat History (Messages), But There is a Problem!
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def get_assistant_answer(user_prompt: str) -> str:
#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# # New
# # messages = []
# messages = [{"role": "assistant", "content": "Hello, I'm Amir. How can I help you?"}]

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     # New
#     messages.append({"role": "user", "content": user_prompt})
#     assistant_answer: str = get_assistant_answer(user_prompt=user_prompt)
#     messages.append({"role": "assistant", "content": assistant_answer})

# st.write(messages)
# **************************************************


# **************************************************
# Fix the previous problem with session state!
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def get_assistant_answer(user_prompt: str) -> str:
#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     # st.session_state.messages = []
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Hello, I'm Amir. How can I help you?"}
#     ]

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     st.session_state.messages.append({"role": "user", "content": user_prompt})
#     assistant_answer: str = get_assistant_answer(user_prompt=user_prompt)
#     st.session_state.messages.append({"role": "assistant", "content": assistant_answer})

# st.write(st.session_state.messages)
# **************************************************


# **************************************************
# Final Code! (English)
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def get_assistant_answer(user_prompt: str) -> str:
#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Hello, I'm Amir. How can I help you?"}
#     ]

# st.set_page_config(page_title="DT Chatbot", page_icon="👋")

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     st.session_state.messages.append({"role": "user", "content": user_prompt})
#     assistant_answer: str = get_assistant_answer(user_prompt=user_prompt)
#     st.session_state.messages.append({"role": "assistant", "content": assistant_answer})

# # st.write(st.session_state.messages)
# # for index, message in enumerate(st.session_state.messages):

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])
# **************************************************


# **************************************************
# Final Code! (Persian)
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def get_assistant_answer(user_prompt: str) -> str:
#     assistant_answer: str = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "assistant", "content": "سلام! من امیر هستم، چه کمکی می‌تونم بکنم؟"}
#     ]

# st.set_page_config(page_title="DT Chatbot", page_icon="👋", layout="wide")

# STREAMLIT_STYLE: str = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container, section, input, textarea {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """

# st.markdown(body=STREAMLIT_STYLE, unsafe_allow_html=True)

# with st.sidebar:
#     st.subheader(body="تنظیمات", divider="rainbow")

# st.header(body="به ربات امیر وزیری خوش آمدید!", divider="rainbow")

# user_prompt: str | None = st.chat_input(
#     placeholder="لطفا سوال خودتان را اینجا بپرسید..."
# )

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     st.session_state.messages.append({"role": "user", "content": user_prompt})
#     assistant_answer: str = get_assistant_answer(user_prompt=user_prompt)
#     st.session_state.messages.append({"role": "assistant", "content": assistant_answer})

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])
# **************************************************


# **************************************************
# import streamlit as st
# import chatbot_constants as constants
# import chatbot_functions as functions

# functions.set_page_config()
# functions.initial_session_state()

# with st.sidebar:
#     st.subheader(body=constants.SETTINGS, divider="rainbow")

#     st.session_state.model_name = st.radio(
#         index=0,
#         options=constants.MODELS,
#         label=constants.SELECT_YOUR_MODEL,
#     ).strip()

#     st.write(constants.SELECTED_MODEL, st.session_state.model_name)
#     st.divider()

#     st.markdown(body=constants.ABOUT, unsafe_allow_html=True)
#     st.divider()

# st.header(body=constants.PAGE_HEADER, divider="rainbow")

# if not st.session_state.model_name:
#     st.error(body=constants.ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME)

# if st.session_state.model_name:
#     user_prompt: str | None = st.chat_input(
#         placeholder=constants.USER_PROMPT_PLACEHOLDER
#     )

#     if user_prompt:
#         user_prompt = user_prompt.strip()

#     if user_prompt:
#         st.session_state.messages.append({"role": "user", "content": user_prompt})
#         assistant_answer = functions.get_assistant_answer(user_prompt=user_prompt)
#         st.session_state.messages.append(
#             {"role": "assistant", "content": assistant_answer}
#         )

#     for index, message in enumerate(st.session_state.messages):
#         if message["role"] == "user":
#             with st.chat_message(name=constants.USER):
#                 st.write(message["content"])
#         elif message["role"] == "assistant":
#             with st.chat_message(name=constants.AI):
#                 st.write(message["content"])
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# # data_frame = pd.read_csv("./data/users.csv")
# data_frame = pd.read_csv("./data/movies.csv")
# st.write(data_frame)
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# st.title(body="Working with Pandas!")

# data_frame = pd.DataFrame(
#     {
#         "Name": ["Alice", "Bob", "Charlie", "David"],
#         "Age": [25, 32, 37, 45],
#         "Occupation": ["Engineer", "Doctor", "Artist", "Chef"],
#     }
# )

# st.subheader(body="write()")
# st.write(data_frame)
# st.divider()

# st.subheader(body="dataframe()")
# st.dataframe(data=data_frame)
# st.divider()

# st.subheader(body="table() -> Static Table")
# st.table(data=data_frame)
# st.divider()

# st.subheader(body="data_editor() -> Editable Table")
# editable_data_frame = st.data_editor(data=data_frame)
# print(editable_data_frame)
# st.divider()

# st.subheader(body="Metrics")
# st.metric(label="Total Rows", value=len(data_frame))
# st.metric(label="Average Age", value=round(data_frame["Age"].mean(), 1))

# st.subheader(body="JSON and Dictionary")
# sample_dictionary = {
#     "name": "Amir",
#     "age": 52,
#     "skills": {"C#", "Python", "AI", "Cyber Security"},
# }

# st.subheader(body="write()")
# st.write(sample_dictionary)

# st.subheader(body="json()")
# st.json(body=sample_dictionary)

# st.divider()
# st.write("Data:", sample_dictionary)
# **************************************************

# **************************************************
# *** Multipage App
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.header(body="Welcome to Amir Site!", divider="rainbow")

# st.link_button(label="About", url="/about")
# st.link_button(label="Contact", url="/contact")
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.header(body="Amir", divider="rainbow")

# # data_frame = yf.download(tickers="AAPL", period="1d", interval="1m")
# data_frame = yf.download(tickers="AAPL", start="2024-01-01", end="2024-01-31")

# st.table(data=data_frame)
# st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Amir")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.selectbox(label="Select a ticker", options=tickers, index=1)

# if dropdown:
#     st.write(dropdown)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Amir")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)
# # dropdown = st.multiselect(label="Select tickers", options=tickers, default=["ETH-USD"])

# if len(dropdown) > 0:
#     # st.write(dropdown)
#     for item in dropdown:
#         st.write(item)
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.title(body="Amir")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)

# start_date = st.date_input(label="Start Date", value="today")
# end_date = st.date_input(label="End Date", value="today")

# if len(dropdown) > 0:
#     data_frame = yf.download(tickers=dropdown, start=start_date, end=end_date)

#     st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# https://www.varzesh3.com
# https://www.varzesh3.com/news
# https://search-api.varzesh3.com/v1.0/query?q=طارمی
# **************************************************
# import os
# import requests

# os.system(command="cls")

# url = "https://search-api.varzesh3.com/v1.0/query?q=طارمی"

# assistant_answer = requests.get(url=url)

# print("-" * 50)
# print("assistant_answer:", assistant_answer)
# print("-" * 50)
# print("assistant_answer.status_code:", assistant_answer.status_code)
# print("-" * 50)
# print("assistant_answer.encoding:", assistant_answer.encoding)
# print("-" * 50)
# print("assistant_answer.headers['content-type']:", assistant_answer.headers["content-type"])
# print("-" * 50)

# if assistant_answer.status_code == 200:
#     print("assistant_answer.text:")
#     print()
#     print(assistant_answer.text)  # Note: -> "
#     print("-" * 50)
#     print("assistant_answer.json():")
#     print()
#     print(assistant_answer.json())  # Note: -> '
#     print("-" * 50)

#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         row_index = index + 1

#         id = item["id"]
#         title = item["title"]
#         published_on = item["publishedOn"]

#         message = f"{row_index}: id: {id} - Published On: {published_on} - {title}"

#         print(message)
# **************************************************

# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# st.title(body="Search in Varzesh3 Site")

# search = st.text_input(label="Search")

# url = f"{base_url}{search}"
# assistant_answer = requests.get(url=url)

# if assistant_answer.status_code == 200:
#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         #         message = f"""
#         # ### {title}
#         # - {short_description}
#         # - زمان انتشار: {persian_published_on}
#         # """

#         #         st.write(message)

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# https://www.cdnfonts.com/iransansx.font
# https://www.cdnfonts.com/iranian-sans.font
# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# streamlit_style = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """

# st.markdown(body=streamlit_style, unsafe_allow_html=True)

# st.title(body="جستجو در سایت ورزش سه")

# search = st.text_input(label="جستجو")

# url = f"{base_url}{search}"
# assistant_answer = requests.get(url=url)

# if assistant_answer.status_code == 200:
#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import streamlit as st

# st.set_page_config(page_title="Amir Vaziry", page_icon="👋", layout="wide")

# with st.container():
#     st.title("👋 Welcome to Amir's Streamlit App!")
#     st.subheader("👋 Welcome to Amir's Streamlit App!")
#     st.write("Hello, World! :wave:")
#     st.write("[Learn More >](https://IranianExperts.ir)")

# with st.container():
#     st.write("---")

#     left_column, right_column = st.columns(2)

#     with left_column:
#         st.header("Amir Vaziry")
#         st.write("##")
#         st.write(
#             """
# I am a student at the University of Tehran.
# I take courses in Computer Science and Mathematics.
# I teach:
# - Python
# - C++
# - C#
# - Java
# """)

#     with right_column:
#         st.header("Amir Vaziry")
# **************************************************

# **************************************************
# import streamlit as st

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Amir's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# with st.sidebar:
#     st.header("About")
#     st.write("This is my first app!")

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Amir's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************