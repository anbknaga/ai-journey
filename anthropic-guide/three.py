from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

convo_history = []

while True:
    input_1 = input("What's your input?: ")

    if input_1.lower() == "quit":
        print("Conversation ended. Thank you for chatting \n")
        break
    
    convo_history.append({"role": "user", "content": input_1})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=400,
        messages=convo_history
    )

    claude_response = response.content[0].text

    print(f"\nAssistant Response: ", claude_response, "\n")
    convo_history.append({"role": "assistant", "content": claude_response})

  