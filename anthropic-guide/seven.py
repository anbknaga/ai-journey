import os
import asyncio
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not set in .env file")

client = AsyncAnthropic(api_key=api_key)

green = '\033[32m'
reset = '\033[0m'

class MyStream:
    def __init__(self):
        self.accumulated_text = ""

    async def on_text(self, text, snapshot):
        self.accumulated_text += text
        print(green + text + reset, end='', flush=True)

    async def on_stream_event(self, event):
        print("\non_event fired:", event)

async def streaming_events_demo():
    stream_handler = MyStream()

    async with await client.messages.create(
        model="claude-3-opus-20240229",
        messages=[{"role": "user", "content": "Generate a 5-word poem"}],
        max_tokens=1024,
        stream=True,
    ) as stream:
        async for event in stream:
            if event.type == "content_block_delta" and hasattr(event.delta, "text"):
                await stream_handler.on_text(event.delta.text, event)
            else:
                await stream_handler.on_stream_event(event)

    print("\n\n✅ Final accumulated response:", stream_handler.accumulated_text)

if __name__ == "__main__":
    asyncio.run(streaming_events_demo())
