'''Write a function called generate_questions that does the following:

Takes two parameters: topic and num_questions
Generates num_questions thought-provoking questions about the provided topic as a numbered list
Prints the generated questions
'''
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

def generate_questions(topic, num_questions):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=999,
        temperature=0.7,
        system="You are an expert at life goals and carrer happiness. You will answer the {topic} asked of you. " \
        "Your response will be in the form of questions with numbered list." \
        "You will just response with the main answer without any thoughts accompanying it.",
        stop_sequences=[f"{num_questions + 1}"],
        messages=[
            {"role": "user", "content": topic},
        ]
    )
    print(response.content[0].text)

generate_questions("Ultimate need of life", 2)

