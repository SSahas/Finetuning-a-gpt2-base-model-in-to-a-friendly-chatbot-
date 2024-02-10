from fastapi import FastAPI

from get_llm_response import get_repsonse_from_llm
from pydantic import BaseModel
from dbms import Clients


class Input(BaseModel):
    text: str


app = FastAPI()

clients = Clients()


@app.get('/prediction')
def get_prediction(question: Input):

    response = get_repsonse_from_llm(question.text)
    data = [{"input_text": question.text, "AI_Response": response}]
    clients.insert_user(data)

    return response
