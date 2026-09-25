from state import EmailState

def route_email(state: EmailState) -> str:
    """Déterminer la prochaine étape basée sur la classification en spam"""
    if state["is_spam"]:
        return "spam"
    else:
        return "legitimate"