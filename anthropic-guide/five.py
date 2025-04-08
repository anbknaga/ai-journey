
from dotenv import load_dotenv
from anthropic import Anthropic
import time

load_dotenv()

client = Anthropic()

start_time = time.time()

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user",
         "content": "Write me a long essay explain what Kelsier is upto in Stormlight archive"}
    ],
    temperature=0,
    stream=True,
)

for event in response:
    if event.type == "content_block_delta":
        print(event.delta.text, end="", flush=True)
    
    elif event.type == "message_start":
        print(f"{event.message.usage.input_tokens}")

    elif event.type == "message_delta":
        print(f'{event.usage.output_tokens}, end="", flush=True')

response_time = time.time() - start_time

print(f"Time to receive first token: {response_time:.3f} seconds")
print(f"Time to recieve complete response: {response_time:.3f} seconds")
print(f"Total tokens generated: {response.usage.output_tokens}")
    