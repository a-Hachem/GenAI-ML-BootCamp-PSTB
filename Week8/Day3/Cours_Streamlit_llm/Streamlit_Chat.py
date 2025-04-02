# import streamlit as st

# with st.chat_message("user"):
#      st.write("Hello 👋")

# import streamlit as st
# import numpy as np

# with st.chat_message("assistant"):
#     st.write("Hello human")
#     st.bar_chart(np.random.randn(30, 3))


# import streamlit as st
# import numpy as np

# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))

# 2.3 Collecte des entrées avec st.chat_input
# La fonction st.chat_input affiche un champ de saisie de chat collant, permettant aux utilisateurs de saisir un message en bas de l'interface.



# import streamlit as st

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")


# Il s’agit d’un moyen simple de capturer les entrées des utilisateurs dans un format de chatbot.

import streamlit as st
import random
import time

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
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello there! How can I assist you today?",
#             "Hi, human! Is there anything I can help you with?",
#             "Do you need help?",
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# # Display assistant response in chat message container
# with st.chat_message("assistant"):
#     response = st.write_stream(response_generator())
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st
import random

# Fonction pour simuler une réponse du bot
def generate_response():
    return random.choice([
        "Hello there! How can I assist you today?",
        "Hi, human! Is there anything I can help you with?",
        "Do you need help?",
    ])

# Titre (une seule fois)
st.title("Simple chat")

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affiche l’historique
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Zone de saisie avec clé
user_input = st.chat_input("What is up?", key="unique_chat_input")

# Si l’utilisateur envoie un message
if user_input:
    # Affiche et enregistre le message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Génére la réponse
    bot_response = generate_response()
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)


    # Génère la réponse en streaming (mot par mot)
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        for word in response_generator():
            full_response += word
            response_placeholder.markdown(full_response)

    # Ajoute la réponse complète à l’historique
    st.session_state.messages.append({"role": "assistant", "content": full_response})

