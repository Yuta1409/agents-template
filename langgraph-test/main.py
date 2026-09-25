from state_graph import compiled_graph

# Exemple d'email légitime
legitimate_email = {
    "sender": "john.smith@example.com",
    "subject": "Question sur vos services",
    "body": "Cher M. Hugg, J'ai été référé à vous par un collègue et je suis intéressé à en savoir plus sur vos services de conseil. Pourrions-nous programmer un appel la semaine prochaine ? Meilleures salutations, John Smith"
}

# Exemple d'email spam
spam_email = {
    "sender": "winner@lottery-intl.com",
    "subject": "VOUS AVEZ GAGNÉ 5 000 000 $ !!!",
    "body": "FÉLICITATIONS ! Vous avez été sélectionné comme gagnant de notre loterie internationale ! Pour réclamer votre prix de 5 000 000 $, veuillez nous envoyer vos coordonnées bancaires et des frais de traitement de 100 $."
}

# Traiter l'email légitime
print("\nTraitement de l'email légitime...")
legitimate_result = compiled_graph.invoke({
    "email": legitimate_email,
    "is_spam": None,
    "spam_reason": None,
    "email_category": None,
    "email_draft": None,
    "messages": []
})

# Traiter l'email spam
print("\nTraitement de l'email spam...")
spam_result = compiled_graph.invoke({
    "email": spam_email,
    "is_spam": None,
    "spam_reason": None,
    "email_category": None,
    "email_draft": None,
    "messages": []
})

from langfuse.langchain import CallbackHandler

# Initialiser le CallbackHandler Langfuse pour LangGraph/Langchain (traçage)
langfuse_handler = CallbackHandler()

# Traiter l'email légitime
legitimate_result = compiled_graph.invoke(
    input={"email": legitimate_email, "is_spam": None, "spam_reason": None, "email_category": None, "email_draft": None, "messages": []},
    config={"callbacks": [langfuse_handler]}
)

# Traiter l'email spam
spam_result = compiled_graph.invoke(
    input={"email": spam_email, "is_spam": None, "spam_reason": None, "email_category": None, "email_draft": None, "messages": []},
    config={"callbacks": [langfuse_handler]}
)
