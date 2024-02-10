
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

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # response = st.write(response_generator(prompt))
        response = response_generator(prompt)
        st.write(response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})