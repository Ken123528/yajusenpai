from openai import api_key
import os
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()
def main():
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME", "gemma4:26b"),
        base_url=os.getenv("OPENAI_API_BASE", "http://203.71.78.31:8000/v1"),
        api_key=os.getenv("OPENAI_API_KEY", "sk-12345678"),
        temperature=0.0,
    )
    
    agent_name = "yajusenpai"
    print(f"Agent {agent_name} initialized with {llm.model_name}")

if __name__ == "__main__":
    main()
    load_dotenv()
    api_key=os.getenv("OPENAI_API_KEY")
    if api_key:
        print("OPENAI_API_KEY:已設定")
    else:
        print("OPENAI_API_KEY:未設定")
    
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME", "gemma4:26b"),
        base_url=os.getenv("OPENAI_API_BASE", "http://203.71.78.31:8000/v1"),
        api_key=os.getenv("OPENAI_API_KEY", "sk-12345678"),
        temperature=0.7,
    )
    response = llm.invoke("你好，請自我介紹")
    while True:   
        user_input = input("You: ")
        if user_input == "":
            continue
        if user_input == "tiuq":
            break
        response = llm.invoke(user_input)
        print(response.content)
    