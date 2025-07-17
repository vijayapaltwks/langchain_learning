from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Load environment variables from .env
load_dotenv()

# Create a ChatAnthropic model
model = ChatAnthropic(model="claude-3-opus-20240229")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)
# prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
# print(prompt)
# result = model.invoke("What is 81 divided by 9?")

chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"topic": "lawyers", "joke_count": 3})
print(result)
