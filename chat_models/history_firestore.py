
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_anthropic import ChatAnthropic

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project
    - Copy the project ID
3. Create a Firestore database in the Firebase project
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""

load_dotenv()

# Setup Firebase Firestore
PROJECT_ID = "v-llm-chat-firestore"
COLLECTION_NAME = "chat_history"


class HistoryFirestore:
    def __init__(self, session_id="session2"):
        self.collection_name = COLLECTION_NAME
        self.session_id = session_id
        self.client = firestore.Client(project=PROJECT_ID)
        self.chat_history = FirestoreChatMessageHistory(
            session_id=self.session_id,
            collection=self.collection_name,
            client=self.client,
        )

    async def get_messages(self):
        # Return messages as a list of dicts for Chainlit
        messages = []
        for msg in self.chat_history.messages:
            if hasattr(msg, 'content'):
                sender = 'user' if msg.__class__.__name__ == 'HumanMessage' else 'claude'
                messages.append({'text': msg.content, 'sender': sender})
        return messages

    async def save_message(self, text, sender="user"):
        # Save message to Firestore
        if sender == "user":
            self.chat_history.add_user_message(text)
        else:
            self.chat_history.add_ai_message(text)
