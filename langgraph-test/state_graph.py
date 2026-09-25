from state import EmailState
from node import read_email, classify_email, handle_spam, draft_response, notify_mr_hugg
from route import route_email
from langgraph.graph import StateGraph, START, END


# Créer le graphe
email_graph = StateGraph(EmailState)

# Ajouter les nœuds
email_graph.add_node("read_email", read_email)
email_graph.add_node("classify_email", classify_email)
email_graph.add_node("handle_spam", handle_spam)
email_graph.add_node("draft_response", draft_response)
email_graph.add_node("notify_mr_hugg", notify_mr_hugg)

# Commencer les arêtes
email_graph.add_edge(START, "read_email")
# Ajouter les arêtes - définir le flux
email_graph.add_edge("read_email", "classify_email")

# Ajouter l'embranchement conditionnel depuis classify_email
email_graph.add_conditional_edges(
    "classify_email",
    route_email,
    {
        "spam": "handle_spam",
        "legitimate": "draft_response"
    }
)

# Ajouter les arêtes finales
email_graph.add_edge("handle_spam", END)
email_graph.add_edge("draft_response", "notify_mr_hugg")
email_graph.add_edge("notify_mr_hugg", END)

# Compiler le graphe
compiled_graph = email_graph.compile()