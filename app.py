import chainlit as cl
from chat_models.history_firestore import HistoryFirestore
from chat_models.conversation import converse_with_claude

# Use Firestore history handler
history = HistoryFirestore(session_id="session2")

# Password authentication callback
@cl.password_auth_callback
def password_auth_callback(username: str, password: str):
    # Simple demo: allow any username/password, but you can add your own logic here
    # For production, check against a user database or hashed password
    if username and password:
        return cl.User(identifier=username)
    return None

@cl.on_chat_start
async def show_history():
    app_user = cl.user_session.get("user")
    await cl.Message(f"Hello {app_user.identifier}").send()
    # Fetch and display previous messages from Firestore
    messages = await history.get_messages()
    # if messages:
    #     summary = "\n".join([f"**{msg['sender'].capitalize()}:** {msg['text']}" for msg in messages])
    #     await cl.Message(f"**Chat History:**\n{summary}").send()
    for msg in messages:
        await cl.Message(
            content=msg['text'],
            author=msg.get('sender', 'user')
        ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    await history.save_message(message.content, sender="user")
    response = await converse_with_claude(message.content)
    await history.save_message(response, sender="claude")
    await cl.Message(content=response, author="claude").send()
