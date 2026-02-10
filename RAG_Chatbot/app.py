from flask import Flask, request, render_template_string
from rag import rag_answer

app = Flask(__name__)

chat_history = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>RAG Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #343541;
            color: white;
            margin: 0;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
            height: 90vh;
            overflow-y: auto;
            padding: 20px;
        }
        .user {
            text-align: right;
            margin: 10px;
        }
        .user span {
            background: #0b93f6;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        }
        .bot {
            text-align: left;
            margin: 10px;
        }
        .bot span {
            background: #444654;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        }
        .input-box {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: #40414f;
            padding: 15px;
        }
        input {
            width: 80%;
            padding: 10px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px;
            border: none;
            background: #19c37d;
            color: black;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div class="chat-container">
    {% for role, msg in chat_history %}
        {% if role == 'user' %}
            <div class="user"><span>{{ msg }}</span></div>
        {% else %}
            <div class="bot"><span>{{ msg }}</span></div>
        {% endif %}
    {% endfor %}
</div>

<div class="input-box">
    <form method="post">
        <input name="question" placeholder="Ask something..." required />
        <button type="submit">Send</button>
    </form>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        question = request.form["question"]
        answer = rag_answer(question)

        chat_history.append(("user", question))
        chat_history.append(("bot", answer))

    return render_template_string(HTML_TEMPLATE, chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
