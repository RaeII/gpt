# Bing,GetGpt,DeepAi

from flask import Flask, request, jsonify
import g4f
from pydantic import BaseModel
from typing import List

class gptObject(BaseModel):
    messages: List[object]

def gpt4Bing(data: gptObject):
    print('\n========\n == BING == \n=========\n')
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4,messages=data.messages,provider=g4f.Provider.Bing)
    return response
    
def gpt3_16k_0613(data: gptObject):
    print('\n=============\n== GPT 16k 0613==\n=============\n')
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_35_turbo_16k_0613, messages=data.messages,provider=g4f.Provider.EasyChat)
    return response
    
# 
# === API ===
# 

app = Flask(__name__)

@app.route('/api/gpt3/16k_0613', methods=['POST'])
def chatCompletionGpt3_16k_0613():
    try:

        data = request.get_json()
        response = gpt3_16k_0613(gptObject(**data))
        return jsonify({'message':response})
    
    except Exception as e:
        errorMessage = str(e)
        print(e)
        return jsonify({'error':errorMessage})
        
@app.route('/api/gpt4/bing', methods=['POST'])
def chatCompletionGpt4Bing():
    try:

        data = request.get_json()
        response = gpt4Bing(gptObject(**data))
        return jsonify(response)
    
    except Exception as e:
        errorMessage = str(e)
        print(e)
        return jsonify({'error':errorMessage})

if __name__ == '__main__':
    app.run()