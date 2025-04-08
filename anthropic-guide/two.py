from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def translate(word, language):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=400,
        messages=[
            {"role": "user", "content": f"Translate {word} into the {language}." 
             "Remember to just output the translated word directly wihtout any of the explnations from you"
             "Also next to the translated word add the pronuniciation of the word in english in brackets"}
        ]
    )

    return response.content[0].text

abc = translate("hello", "Spanish")
print(abc)