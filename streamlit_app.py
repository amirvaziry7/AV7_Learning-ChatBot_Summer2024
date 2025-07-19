import streamlit as st
import stremalit_tools as STTOOLS





st.set_page_config(page_title="WellCome To My ChatBot",page_icon="👋")

st.header(body="WellCome To My ChatBot DearFriend")


message=[
    {"role":"system","content":"You are Helpful assitant"}
]
if "messages"  not in st.session_state:
    st.session_state.messages=message


user_message=st.chat_input(placeholder="Please Enter Your Request")

if user_message:
    user_message=user_message.strip()
    st.session_state.messages.append(
    {"role":"user","content":user_message}
    )
    response=STTOOLS.CreateResponse(user_message)

    st.session_state.messages.append(
    {"role":"assistant","content":response}
    )   

for txt in st.session_state.messages:
    
    if(txt["role"]=="user"):
        if(txt["content"]!=None):
            with st.chat_message("user"):
                st.write(txt["content"])
    elif(txt["role"]=="assistant"):
        if(txt["content"]!="This is your Prompt None"):
            with st.chat_message("ai"):
                st.write(txt["content"])

