#Importing the libraries
import streamlit as st
import openai

#Setting the API key of OpenAI
openai.api_key = st.secrets["OPEN_API_KEY"]

st.title("Einfacher Chatbot")

#Initializing the chat history if it doesn't already exist
if "messages" not in st.session_state:
    st.session_state.messages = []

#Showing the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Responding to the user's input
if prompt := st.chat_input("Schreibe deine Nachricht:"):
    #Showing the user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #Sending the input to GPT-4 and receiving the response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du bist ein hilfsbereiter Chatbot."},
            {"role": "user", "content": prompt}
        ]
    )

    #Showing the response of the chatbot
    bot_message = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": bot_message})
    with st.chat_message("assistant"):
        st.markdown(bot_message)
