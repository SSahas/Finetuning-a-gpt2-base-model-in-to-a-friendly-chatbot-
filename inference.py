
import time
import random
import streamlit as st
import requests
import json

import asyncio

url = "http://localhost:8000/prediction"


headers = {}

def response_generator(text):
    payload = json.dumps({"text": text})
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


st.title("Simple chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = response_generator(prompt)
        st.write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
