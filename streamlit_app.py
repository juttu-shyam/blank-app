import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# from langchain_ollama import ChatOllama
# llm= ChatOllama(model='llama3.2')
# history=[{'role':'system','content':'- you are a coding teacher - answer each question in two lines'}]
# while True:
#     question=input()
#     history.append({'role':'user','content':question})
#     responce=llm.invoke(history).content
#     history.append({'role':'assistant','content':responce})
#     print(responce)
