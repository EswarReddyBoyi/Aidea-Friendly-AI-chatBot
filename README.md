
# 🤖 Aidea – Friendly AI Chatbot

**Aidea (AI + Idea)** is a sleek, animated, and mobile-friendly chatbot web app powered by **LLaMA-3-70B** via **Together AI API**. Designed with a floating UI, scroll effects, code block formatting, and popup tips — it’s your friendly assistant for ideas, code help, learning, and more.

> 🎯 Live Demo: [https://aidea-chatbot.onrender.com](https://aidea-chatbot.onrender.com)

---

## 🌟 Features

- 🧠 Powered by Together AI's LLaMA-3 70B (via API)
- 💬 Live chat with animated floating bubbles
- 📱 Fully responsive (desktop & mobile)
- 🎨 Transparent, custom-styled chat UI
- 🧾 Code block replies with **copy button**
- 🔔 Pop-up tips like “Don’t be shy, just say hi!”
- ⏬ Scrolls smoothly and auto-focuses on new messages
- 🌐 Deployed for free on [Render.com](https://render.com)

---

## 📁 Folder Structure

```
aidea-chatbot/
│
├── static/
│   └── bg.jpg               # Background image
│
├── templates/
│   └── index.html           # Main chatbot UI
│
├── .env                     # Environment file (API key)
├── app.py                   # Flask backend logic
├── requirements.txt         # Python dependencies
└── README.md                # Project info (this file)
```

---

## 🚀 Local Development

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/your-username/aidea-chatbot.git
cd aidea-chatbot
```

### 2. 🧪 Create `.env` file

```bash
TOGETHER_API_KEY=your_api_key_here
```

> 🔐 Get your Together API key from:  
> https://api.together.xyz/settings/api-keys

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 🧠 Run the Flask App

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## 🧠 How It Works

### ✅ API Payload Example

```json
{
  "model": "meta-llama/Llama-3-70b-chat-hf",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a Python code to reverse a string."}
  ],
  "temperature": 0.7,
  "max_tokens": 300
}
```

### ✅ Flask Endpoint

```python
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    ...
    return jsonify({'reply': bot_reply})
```

---

## 📸 Screenshots

| Desktop View | Mobile View |
|--------------|-------------|
|![Screenshot 2025-07-05 234228](https://github.com/user-attachments/assets/51470fff-f7ba-4873-9918-1fd5b497e741) ![phn](https://github.com/user-attachments/assets/fdba818b-1fe0-456c-bfd6-d231fd63794f)
![bg](https://github.com/user-attachments/assets/801edd15-0241-44f5-b59f-4fa34a5aa9b3)
 | Responsive layout with popups & floating chat |

---

## 🛠 Requirements

```
Flask
requests
python-dotenv
```

Use this for `requirements.txt`:

```txt
Flask
requests
python-dotenv
```

---

## 🙌 Credits

- 👨‍💻 Developer: **Eswar Reddy Boyi**
- 🤖 AI Model: **LLaMA-3 70B** by Together AI
- 💻 Stack: Python Flask + HTML/CSS/JS

---

## ⚖️ License

© 2025 **Eswar Reddy Boyi**  
All rights reserved.  
Free for learning and personal use. Attribution required if forked publicly.

---

## 📬 Contact

Want to contribute, collaborate or improve?  
📧 Email: [eswarboyi7@gmail.com](mailto:eswarboyi7@gmail.com)  
🌐 LinkedIn: [linkedin.com/in/eswarboyi](https://linkedin.com/in/eswarboyi](https://www.linkedin.com/in/eswar-boyi-795250253?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

> 🧠 **Aidea** – A smart buddy who understands you and responds like a friend. Ask code, jokes, doubts or ideas. Always ready to help!
