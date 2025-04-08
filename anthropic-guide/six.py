from anthropic import AsyncAnthropic
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = AsyncAnthropic()

async def streaming_with_helpers():
    async with client.messages.stream(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "Generate a long & beautiful poem about waterfalls"
            }
        ],
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = await stream.get_final_message()
    print(final_message)

asyncio.run(streaming_with_helpers())