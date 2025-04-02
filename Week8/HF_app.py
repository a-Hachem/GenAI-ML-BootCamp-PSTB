import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Chargement de la clé HF depuis le .env
load_dotenv()
hf_token = os.getenv("HF_API_KEY")

# Fonction de construction du prompt au format Zephyr
def build_prompt(messages):
    prompt = ""
    for msg in messages:
        if msg["role"] == "user":
            prompt += f"<|user|>\n{msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"<|assistant|>\n{msg['content']}\n"
    prompt += "<|assistant|>\n"
    return prompt

#  Appel à l'API Hugging Face pour le modèle Zephyr
def call_zephyr(prompt_text):
    url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"
    headers = {"Authorization": f"Bearer {hf_token}"}
    payload = {
        "inputs": prompt_text,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "top_p": 0.9,
            "repetition_penalty": 1.1
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"].split("<|assistant|>\n")[-1].strip()
    else:
        return f"Erreur {response.status_code} : {response.text}"

# Interface Streamlit
st.title(" Chat avec Zephyr (Hugging Face)")

#  Historique de conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

#  Affichage des anciens messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#  Saisie utilisateur
prompt = st.chat_input("Posez votre question à Zephyr...")

# Si message saisi
if prompt:
    # 1. Ajout à l’historique utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Génération Zephyr
    with st.chat_message("assistant"):
        with st.spinner("Zephyr réfléchit..."):
            full_prompt = build_prompt(st.session_state.messages)
            response = call_zephyr(full_prompt)
            st.markdown(response)

    # 3. Ajout de la réponse à l'historique
    st.session_state.messages.append({"role": "assistant", "content": response})
