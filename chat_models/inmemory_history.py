class InMemoryHistory:
    def __init__(self):
        self.messages = []

    async def get_messages(self):
        # Return messages as a list of dicts
        return [
            {'text': msg['text'], 'sender': msg['sender']} for msg in self.messages
        ]

    async def save_message(self, text, sender="user"):
        self.messages.append({'text': text, 'sender': sender})
