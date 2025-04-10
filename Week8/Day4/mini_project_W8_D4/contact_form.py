import streamlit as st
import pandas as pd
from datetime import datetime

def display_contact_form():
    st.subheader("📞 Vos coordonnées")

    with st.form("contact_form"):
        name = st.text_input("Votre nom")
        email = st.text_input("Votre e-mail")
        phone = st.text_input("Votre numéro de téléphone")
        submit = st.form_submit_button("Envoyer")

        if submit:
            save_contact_info(name, email, phone)
            st.success("✅ Merci ! Nous vous contacterons bientôt.")

def save_contact_info(name, email, phone):
    contact = {
        "Nom": name,
        "E-mail": email,
        "Téléphone": phone,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([contact])
    df.to_csv("contacts.csv", mode="a", index=False, header=not file_exists("contacts.csv"))

def file_exists(path):
    try:
        with open(path, "r"):
            return True
    except FileNotFoundError:
        return False
