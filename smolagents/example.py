from smolagents import CodeAgent, DuckDuckGoSearchTool, FinalAnswerTool, InferenceClientModel, Tool, tool, VisitWebpageTool

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggère un menu basé sur l'occasion.
    Args:
        occasion: Le type d'occasion pour la fête.
    """
    if occasion == "casual":
        return "Pizza, collations et boissons."
    elif occasion == "formal":
        return "Dîner 3 services avec vin et dessert."
    elif occasion == "superhero":
        return "Buffet avec nourriture énergétique et saine."
    else:
        return "Menu personnalisé pour le majordome."

@tool
def catering_service_tool(query: str) -> str:
    """
    Cet outil renvoie le service de restauration le mieux noté à Gotham City.
    
    Args:
        query: Un terme de recherche pour trouver des services de restauration.
    """
    # Exemple de liste de services de restauration et leurs notes
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }
    
    # Trouver le service de restauration le mieux noté (simuler le filtrage de requête de recherche)
    best_service = max(services, key=services.get)
    
    return best_service

class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = """
    Cet outil suggère des idées créatives de fête sur le thème des super-héros basées sur une catégorie.
    Il renvoie une idée de thème de fête unique."""
    
    inputs = {
        "category": {
            "type": "string",
            "description": "Le type de fête de super-héros (par ex., 'héros classiques', 'mascarade de méchants', 'Gotham futuriste').",
        }
    }
    
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Gala de la Justice League : Les invités viennent habillés comme leurs héros DC préférés avec des cocktails thématiques comme 'Le Punch Kryptonite'.",
            "villain masquerade": "Bal des Voyous de Gotham : Une mascarade mystérieuse où les invités s'habillent en méchants classiques de Batman.",
            "futuristic Gotham": "Nuit Neo-Gotham : Une fête de style cyberpunk inspirée de Batman Beyond, avec des décorations néon et des gadgets futuristes."
        }
        
        return themes.get(category.lower(), "Idée de fête thématique non trouvée. Essayez 'héros classiques', 'mascarade de méchants', ou 'Gotham futuriste'.")


# Alfred, le majordome, préparant le menu pour la fête
agent = CodeAgent(
    tools=[
        DuckDuckGoSearchTool(), 
        VisitWebpageTool(),
        suggest_menu,
        catering_service_tool,
        SuperheroPartyThemeTool(),
	FinalAnswerTool()
    ], 
    model=InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"),
    max_steps=10,
    verbosity_level=2
)

agent.run("Donne-moi la meilleure playlist pour une fête au manoir des Wayne. L'idée de la fête est un thème 'mascarade de méchants'")