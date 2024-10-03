import openai
from api_keys import CHATGPT_API_KEY

openai.api_key = CHATGPT_API_KEY

def ask_chad(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use a less resource-intensive model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ],
        max_tokens=150,
        top_p=0.95
    )
    return ''.join([choice['message']['content'] for choice in response['choices']])