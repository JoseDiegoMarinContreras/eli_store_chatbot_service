from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import EliStoreChatbot

app = Flask(__name__)
CORS(app)

@app.route('/api/chatbot', methods=['POST'])
def chatbot_Service():
    requestContent = request.json
    print(requestContent)
    response = {
        'message': EliStoreChatbot.respond(requestContent['message'])
    }
    return jsonify(response)