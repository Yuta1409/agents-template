from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("Recherche les meilleures recommandations musicales pour une fête au manoir des Wayne.")