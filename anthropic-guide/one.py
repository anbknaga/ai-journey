from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=3000,
    messages=[
        {"role": "user", "content": "Hi, how are you"},
        {"role": "assistant", "content": "I'm fine, how are you?"},
        {"role": "user", "content": "CSK or MI, which team is better"},
        {"role": "assistant", "content": "CSK is better"}
    ]
)

print(response.content[0].text)