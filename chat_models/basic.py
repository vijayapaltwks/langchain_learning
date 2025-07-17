from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env
load_dotenv()

# Create a ChatAnthropic model
model = ChatAnthropic(model="claude-3-opus-20240229")

# Invoke the model with a message

result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
