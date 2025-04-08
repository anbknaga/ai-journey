'''
Write a simple Claude chatbot that uses streaming. The following gif illustrates how it should work. 
Please note that the color-coding of the output is completely optional and 
mostly helps to make the gif readable/watchable:

Input / output 
conversations torage throughout the chat
quit close chat
streaming messages

Green: Claude both cluade name and answers
'''
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

green = '\033[32m'
blue = '\033[34m'
reset = '\033[0m'

def chat_with_chatbot():
    print("Welcome to *** THE CHATBOT ***")
    print("Type 'quit' if you want to close this chatbot")
    print("==============================>")

    conversation_history = []

    while True:
        user_input = input(f"{blue} You: {reset}")

        if user_input == 'quit':
            print("*** Thanks for chatting! ***")
            break

        conversation_history.append({"role": "user", "content": user_input})

        print(f"{green} Claude: {reset}", end="")

        stream = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=100,
            stream=True,
            messages=conversation_history
        )

        claude_response = ""
        for event in stream:
            if event.type == "content_block_delta":
                chunk = event.delta.text
                claude_response += chunk 
                print(f"{green}{chunk}{reset}", end="", flush=True)
        
        print()

        conversation_history.append(({"role": "assistant", "content": claude_response}))

chat_with_chatbot()
