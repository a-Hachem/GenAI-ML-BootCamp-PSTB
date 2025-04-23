
# 🤖 Chatbot PDF avec Gemini, LangChain & FAISS

Ce projet est une application Streamlit de démonstration d’un assistant IA capable de :
- Lire un ou plusieurs fichiers PDF
- Extraire et vectoriser leur contenu
- Répondre à des questions en langage naturel grâce à **Gemini**
- Maintenir une mémoire conversationnelle
- Gérer des demandes de contact via un **formulaire intelligent**

---

## 📷 Aperçu

![Chatbot PDF avec Gemini](./assets/screenshot_chatbot.png)

---

## 🚀 Fonctionnalités

- 📄 Upload de fichiers PDF
- ✂️ Découpage intelligent du texte (LangChain)
- 🧠 Embeddings générés avec `GoogleGenerativeAI`
- 🗃️ Index vectoriel FAISS
- 💬 Assistant conversationnel avec mémoire
- 📞 Formulaire de contact déclenché sur intention “appelle-moi”
- 💾 Sauvegarde des contacts dans `contacts.csv`

---

## 🛠️ Lancer le projet

```bash
# 1. Créer un environnement virtuel
python -m venv my_venv
source my_venv/bin/activate  # ou .venv\Scripts\activate sous Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
streamlit run app.py
```

> N'oubliez pas de créer un fichier `.env` avec votre clé API Gemini :
```
GOOGLE_API_KEY=votre_clé
```

---

## 📂 Structure du projet

```
chatbot_pdf_gemini/
├── app.py
├── pdf_utils.py
├── text_splitter.py
├── embeddings_faiss.py
├── chat_chain.py
├── contact_form.py
├── contacts.csv
├── .env
├── requirements.txt
├── assets/
│   └── screenshot_chatbot.png
```

---

## ✨ Réalisé par

> Aïcha Hachemi– Bootcamp GenAI & Machine Learning 2025 (PSTB)
