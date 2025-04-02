# 🤖 Amazon Review Assistant — Sentiment Classification & Response Generation

This project showcases a complete end-to-end NLP pipeline using LLMs to analyze customer reviews posted on Amazon, classify their sentiment, and generate short, context-aware replies. The pipeline includes model training, generation via prompt engineering, evaluation with NLP metrics, and an interactive Streamlit interface.

---

## 📚 Project Overview

The project is structured into **three main parts**:

### 1. 🔍 Sentiment Classification (Fine-Tuned BERT)

- Objective: Predict the sentiment of customer reviews from the Amazon dataset.
- Preprocessing: Light text cleaning and removal of neutral scores (3/5 ratings).
- Labeling: Sentiment was inferred from the rating (1–2 = negative, 4–5 = positive).
- Models:
  - `bert-base-uncased` with full fine-tuning
  - `bert-base-uncased` with LoRA fine-tuning (PEFT)
- Class imbalance was addressed using **class weights**.
- Final choice: **LoRA model**, due to better generalization and reduced training time.
- Metrics compared: Loss & F1 score

### 2. ✨ Response Generation with LLMs

- Goal: Generate short, friendly replies to Amazon reviews.
- Models used:
  - `flan-t5-small` (lightweight baseline)
  - `HuggingFaceH4/zephyr-7b-beta` (powerful instruction-tuned model)
- Prompt structure:
  - Inputs: `user review`, `detected sentiment`, and `3 similar reviews`
  - The similar reviews were retrieved using **FAISS** (cosine similarity over SentenceTransformers embeddings).
- Generation was done using Hugging Face pipelines.
- Final comparison table generated:
  - BLEU, ROUGE-L, and **Perplexity** scores for Flan vs Zephyr.

### 3. 🖥️ Interactive Streamlit App

- Features:
  - User enters a customer review
  - App detects sentiment with the LoRA fine-tuned BERT model
  - App generates a natural reply using `flan-t5-small`
  - User can manually enter a reference reply
  - BLEU and ROUGE-L scores are computed
  - Simple feedback buttons for user rating (👍 👎)
- Notes:
  - Zephyr is showcased in the notebook for quality comparison but is too large for the local Streamlit deployment
  - Flan-T5 is used in the app for speed and usability

---

## 🚀 How to Run the App

### 🔧 Installation
```bash
pip install -r requirements.txt
```

### ▶️ Run Streamlit
```bash
streamlit run main_app.py
```

Make sure to extract and place the following local models in your `app/` directory:
```
app/
├── bert_sentiment_lora/          # LoRA fine-tuned BERT model for classification
└── flan_t5_small/                # Lightweight generator model
```

---

## 📂 Project Structure
```
├── app/
│   ├── bert_sentiment_lora/
│   └── flan_t5_small/
├── main_app.py                   # Streamlit application
├── requirements.txt              # Environment dependencies
├── README.md                     # Project documentation
```

---

## 📊 Example Output

```text
✍️ User Review:
"great card (32gb) i've always bought sandisk sd cards, and have never been disappointed..."

🧠 Detected Sentiment: positive

💬 AI-Generated Reply:
"Thank you for your continued trust in SanDisk! We're glad this card met your expectations."

🧑‍💬 Reference Reply:
"Thanks for your loyalty! We're happy you're satisfied once again."

📈 BLEU: 0.41 | ROUGE-L: 0.58
```

---

## 🧪 Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- PEFT (LoRA)
- Evaluate (for BLEU, ROUGE, Perplexity)
- FAISS + SentenceTransformers

---

## 🧠 Credits
Developed as part of a training program focused on GenAI, NLP and LLMs. Built and designed by Carole 💡

---

## 📬 Contact
For any questions or feedback, feel free to reach out via GitHub or connect on LinkedIn!
