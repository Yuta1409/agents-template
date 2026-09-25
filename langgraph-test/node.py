from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from state import EmailState
from dotenv import load_dotenv

# Charge le .env à la racine du projet (dossier parent)
load_dotenv()
# Initialiser notre LLM
model = ChatAnthropic(model_name="claude-haiku-4-5-20251001", temperature=0)

def read_email(state: EmailState):
    """Alfred lit et enregistre l'email entrant"""
    email = state["email"]
    
    # Ici nous pourrions faire un prétraitement initial
    print(f"Alfred traite un email de {email['sender']} avec le sujet : {email['subject']}")
    
    # Aucun changement d'état nécessaire ici
    return {}

def classify_email(state: EmailState):
    """Alfred utilise un LLM pour déterminer si l'email est spam ou légitime"""
    email = state["email"]
    
    # Préparer notre prompt pour le LLM
    prompt = f"""
    En tant qu'Alfred le majordome, analysez cet email et déterminez s'il s'agit de spam ou s'il est légitime et doit être porté à l'attention de M. Hugg.
    
    Email :
    De : {email['sender']}
    Sujet : {email['subject']}
    Corps : {email['body']}
    
    Premièrement, détermine si cet email est du spam.
    Réponds par SPAM ou HAM s'il est légitime. Retourne uniquement la réponse.
    Réponse :
    """
    
    # Appeler le LLM
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    
    # La réponse est strictement SPAM ou HAM, le parsing est donc simple
    response_text = response.content.lower()
    is_spam = "spam" in response_text and "ham" not in response_text
    
    # Mettre à jour les messages pour le suivi
    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response.content}
    ]
    
    # Retourner les mises à jour d'état
    return {
        "is_spam": is_spam,
        "messages": new_messages
    }

def handle_spam(state: EmailState):
    """Alfred rejette l'email spam avec une note explicative"""
    print(f"Alfred a marqué l'email comme spam. Raison : {state['spam_reason']}")
    print("L'email a été déplacé dans le dossier spam.")
    
    # Nous avons fini de traiter cet email
    return {}

def draft_response(state: EmailState):
    """Alfred rédige une réponse préliminaire pour les emails légitimes"""
    email = state["email"]
    category = state["email_category"] or "general"
    
    # Préparer notre prompt pour le LLM
    prompt = f"""
    En tant qu'Alfred le majordome, rédige une réponse préliminaire polie à cet email.
    
    email :
    De : {email['sender']}
    Sujet : {email['subject']}
    Corps : {email['body']}
    
    Cet email a été catégorisé comme : {category}
    
    Rédige une réponse brève et professionnelle que M. Hugg peut réviser et personnaliser avant l'envoi.
    """
    
    # Appeler le LLM
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)
    
    # Mettre à jour les messages pour le suivi
    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response.content}
    ]
    
    # Retourner les mises à jour d'état
    return {
        "email_draft": response.content,
        "messages": new_messages
    }

def notify_mr_hugg(state: EmailState):
    """Alfred informe M. Hugg de l'email et présente le brouillon de réponse"""
    email = state["email"]
    
    print("\n" + "="*50)
    print(f"Monsieur, vous avez reçu un email de {email['sender']}.")
    print(f"Sujet : {email['subject']}")
    print(f"Catégorie : {state['email_category']}")
    print("\nJ'ai préparé un brouillon de réponse pour votre révision :")
    print("-"*50)
    print(state["email_draft"])
    print("="*50 + "\n")
    
    # Nous avons fini de traiter cet email
    return {}