from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
from smolagents import CodeAgent, InferenceClientModel
from dotenv import load_dotenv

load_dotenv()

langfuse_client = get_client()

if langfuse_client.auth_check():
    print("Langfuse client is authenticated successfully.")
else :
    print("Langfuse client authentication failed. Please check your keys and try again.")

SmolagentsInstrumentor().instrument()

alfred_agent = CodeAgent.from_hub('sergiopaniego/AlfredAgent', trust_remote_code=True, model=InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"))
alfred_agent.run("Donne-moi la meilleure playlist pour une fête au manoir des Wayne. L'idée de la fête est un thème 'mascarade de méchants'")  