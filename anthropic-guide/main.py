from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=my_api_key)


response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
)
print(response.content[0].text)
