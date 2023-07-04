# Bing,GetGpt,DeepAi

from flask import Flask, request, jsonify
import g4f
from pydantic import BaseModel
from typing import List

class gptObject(BaseModel):
    messages: List[object]

def gpt4Bing(data: gptObject):
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=data.messages)
    return response

app = Flask(__name__)

@app.route('/api/gpt4/bing', methods=['POST'])
def chatCompletionGpt4Bing():
    data = request.get_json()
    response = gpt4Bing(gptObject(**data))
    return jsonify(response)

if __name__ == '__main__':
    app.run()