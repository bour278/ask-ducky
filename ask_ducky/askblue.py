import requests
from api_keys import GEMINI_API_KEY

def ask_blue(query):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": query}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    # Extract the answer from the returned JSON
    answer = response_json.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No answer found')
    return answer