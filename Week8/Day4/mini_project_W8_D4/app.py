# app.py

import streamlit as st
from dotenv import load_dotenv
import os

# Modules personnalisés
from pdf_utils import extract_text_from_pdfs
from text_splitter import split_text
from embeddings_faiss import create_vectorstore
from chat_chain import create_chat_chain

from google.generativeai import list_models
import google.generativeai as genai

from contact_form import display_contact_form


# 1. Chargement de l'environnement (.env)
load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# models = list_models()
# for model in models:
#     print(model.name)


# 2. Config de la page
st.set_page_config(page_title=" PDF Chatbot Gemini", layout="wide")
st.title(" Chatbot PDF avec Gemini, FAISS & LangChain")

# 3. Initialisation de la session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "show_contact_form" not in st.session_state:
    st.session_state.show_contact_form = False

# 4. Barre latérale : Téléversement de fichiers PDF
st.sidebar.header("📎 Téléverser des fichiers PDF")
uploaded_files = st.sidebar.file_uploader("Choisissez un ou plusieurs PDF :", type="pdf", accept_multiple_files=True)

# 5. Traitement des fichiers
if uploaded_files:
    with st.spinner(" Lecture des fichiers..."):
        raw_text = extract_text_from_pdfs(uploaded_files)
        text_chunks = split_text(raw_text)
        vectorstore = create_vectorstore(text_chunks)
        st.session_state.vectorstore = vectorstore
        st.success("PDF analysé et vectorisé avec succès.")

    # Création de la chaîne (si elle n’existe pas déjà)
    if st.session_state.conversation is None:
        st.session_state.conversation = create_chat_chain(vectorstore)

# 6. Interface de chat
st.subheader(" Posez vos questions à propos du ou des PDF")

user_input = st.chat_input("Tapez votre question ici...")

if user_input:
    lower_input = user_input.lower()

    if "call me" in lower_input or "appelle-moi" in lower_input:
        st.session_state.chat_history.append(("Vous", user_input))
        st.session_state.chat_history.append((
            "Bot",
            "📞 Merci pour votre demande ! Veuillez remplir le formulaire ci-dessous pour qu’on puisse vous recontacter."
        ))
        st.session_state.show_contact_form = True  # <-- le drapeau !
    else:
        with st.spinner("💡 Gemini réfléchit..."):
            response = st.session_state.conversation.run(user_input)
            st.session_state.chat_history.append(("Vous", user_input))
            st.session_state.chat_history.append(("Bot", response))

# 7. Affichage du chat
for role, msg in st.session_state.chat_history:
    if role == "Vous":
        st.chat_message("user").markdown(msg)
    else:
        st.chat_message("assistant").markdown(msg)

if st.session_state.show_contact_form:
    with st.chat_message("assistant"):
        display_contact_form()
    st.session_state.show_contact_form = False  # Réinitialiser

