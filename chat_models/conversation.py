from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Create a ChatAnthropic model
model = ChatAnthropic(model="claude-3-haiku-20240307")


# Utility function for Chainlit to converse with Claude
async def converse_with_claude(query, chat_history=None):
    if chat_history is None:
        chat_history = []
        # Set an initial system message (optional)
        system_message = SystemMessage(content="You are a helpful AI assistant.")
        chat_history.append(system_message)
    chat_history.append(HumanMessage(content=query))
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    return response
