import streamlit as st
import random
import time

# Fonction qui génère une réponse aléatoire
def response_generator():
    response = random.choice([
        "Hello there! How can I assist you today?",
        "Hi, human! Is there anything I can help you with?",
        "Do you need help?"
    ])
    for word in response.split():
        yield word + " "
        time.sleep(0.05)  # Pause pour effet de frappe

# Titre
st.title("Simple chat")

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Champ de saisie
user_input = st.chat_input("What is up?", key="chat_input")

# Si un message est envoyé
if user_input:
    # Ajout du message utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Réponse progressive de l’assistant
    full_response = ""
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        for word in response_generator():
            full_response += word
            response_placeholder.markdown(full_response)

    # Ajout à l'historique
    st.session_state.messages.append({"role": "assistant", "content": full_response})
