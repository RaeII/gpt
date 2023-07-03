#Bing,GetGpt,DeepAi

import g4f
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

class gptObject(BaseModel):
    messages: List[object]

def gpt4Bing(data: gptObject):

    print('DATA =>', data,'\n\n')

    messageComplete = ''
    response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
                                     {"role": "user", "content": "hi"}])

    # for message in response:
    #     messageComplete +=message
    #     print(message)
    
    return messageComplete

app = FastAPI()

@app.post("/api/gpt4/bing")
def chatCompletionGpt4Bing(data: gptObject):
    response = gpt4Bing(data)
    return response 