#import langchain
#from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain_community.llms import HuggingFaceHub
from secret_key import huggingface_key

import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = huggingface_key

llm = HuggingFaceHub(repo_id= "google/flan-t5-base", model_kwargs = {"temperature" : 0})


convo = ConversationChain(llm=llm)


def get_repsonse_from_llm(text:str):

    #response = convo.run(text)
    response =  convo.run(text)

    return response