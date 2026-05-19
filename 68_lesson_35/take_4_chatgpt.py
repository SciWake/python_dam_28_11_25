import requests

api_key = ""

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'Ты крутой python программист в области визуализации на plotly'},
        {'role': 'user', 'content': 'Визуализируй мне пожалуйста какие-то данные и дай код на python'}
    ],
    'temperature': 0.7
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

if response.status_code == 200:
    reply = response.json()['choices'][0]['message']['content']
    print(f'Ответ от ChatGPT: {reply}')
else:
    print(f'Ошибка: {response.status_code} - {response.text}')