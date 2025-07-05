from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/Llama-3-70b-chat-hf",  # Or try Mixtral
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }
    
    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)

    try:
        bot_reply = response.json()['choices'][0]['message']['content'].strip()
    except:
        bot_reply = "Error: " + response.text

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
