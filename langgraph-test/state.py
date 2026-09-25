from typing import TypedDict, List, Dict, Any, Optional


class EmailState(TypedDict):
    # L'email en cours de traitement
    email: Dict[str, Any]  # Contient sujet, expéditeur, corps, etc.

    # Catégorie de l'email (enquête, plainte, etc.)
    email_category: Optional[str]

    # Raison pourquoi l'email a été marqué comme spam
    spam_reason: Optional[str]

    # Analyse et décisions
    is_spam: Optional[bool]
    
    # Génération de réponse
    email_draft: Optional[str]
    
    # Métadonnées de traitement
    messages: List[Dict[str, Any]]  # Suivre la conversation avec le LLM pour l'analyse
    