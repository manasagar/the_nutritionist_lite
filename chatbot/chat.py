import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

def bot(text):
    llm = OpenAI(temperature = 0.9)
    return llm(text)