## Objectif général

Créer un assistant basé sur un LLM capable de :
- Résumer un contrat en anglais simple
- Répondre à des questions juridiques comme un expert
- Maintenir le contexte d’une conversation utilisateur
- Évaluer ses propres réponses pour en améliorer la clarté et la fiabilité

---

## Étape 1 : Invite de résumé initiale

###  Ce que le résumé doit contenir :
- **Responsabilités** de chaque partie
- **Conditions de paiement**
- **Clauses de résiliation**
- **Limitations de responsabilité**

###  Prompt (avec chaîne de pensée – CoT) :

```
You are a legal assistant. Read the contract excerpt below and summarize it in clear, simple English.

Before writing the summary, think step-by-step:
1. What does the service provider agree to do?
2. What are the client's payment obligations?
3. When does the contract start and how can it end?
4. What are the limits to the provider's liability?

Now, summarize the key points in a few concise sentences.
Avoid legal jargon. Be clear and neutral.
```

### Exemple de résumé :

The service provider, BrightLine Technologies, will manage the client’s cloud infrastructure.  
This includes monitoring, incident response, and monthly reports.  

The client, NovaWare Systems, will pay $12,000 per month, due within 30 days of each invoice.  
Late payments incur a 2% monthly fee.  

The contract lasts 12 months from March 1, 2025. Either party can end it with 30 days’ notice.  

The provider’s total liability is capped at the amount paid by the client over the past 3 months.  
They are not liable for indirect or consequential damages.

---

## Étape 2 : Questions-réponses juridiques (Role Prompt + CoT)

### Prompt avec rôle et raisonnement :

```
You are a contract lawyer. A user will ask you questions about the service agreement shown earlier.

Answer in simple, professional English. Think step-by-step to ensure clarity and legal accuracy.

If the user asks about a clause:
- Briefly explain what the clause means in practice.
- Clarify the implications for both the client and the provider.
- If relevant, note any timeframes, penalties, or limits.
```

###  Exemple de question :

**User**: Can you explain the liability limitation clause?  
**Assistant**: The provider can’t be held responsible for indirect damages. Also, any claim is limited to the total amount the client paid in the last 3 months.

---

##  Étape 3 : Intégration de la mémoire (context chaining)

###  Objectif : Garder en mémoire le résumé pour contextualiser les réponses suivantes.

###  Méthode choisie : **Transmission préalable du message**

### Prompt simulé :

```
Context:
The contract says that BrightLine manages cloud infrastructure for NovaWare. NovaWare pays $12,000/month. The contract lasts 12 months, and can be ended with 30 days' notice. Liability is capped at 3 months of fees.

Now, continue answering user questions based on this information.

User: What happens if the client doesn't pay on time?
```

###  Réponse attendue :
If the client doesn’t pay within 30 days, they have to pay a 2% penalty for each month the payment is late.

---

##  Étape 4 : Atténuation et Affinement (Auto-réflexion)

###  Prompt d'auto-évaluation :

```
Before sending your answer, take a moment to reflect.

Ask yourself:
- Did I fully understand the user’s question?
- Did I explain the clause in simple, correct language?
- Did I avoid making up new terms or details not found in the contract?
- Is there a clearer or shorter way to say this?

If needed, revise your answer before responding.
```

### (Optionnel) – Multi-agent : critique croisée

```
You are a second legal assistant reviewing the first assistant’s response.
Point out any errors, unclear points, or legal inaccuracies.
Suggest improvements if needed.
```
