
import streamlit as st
from agents import *

def chat_page():
    '''
    Cria a página do chat
    '''

    st.set_page_config(
        page_title="IA do Gary Halbert",
        page_icon="✍️",
    )

    st.markdown("# Converse com o maior guru e galã do marketing de resposta direta!")
    st.image("files/imgs/Gary-Halbert.jpg")
    st.divider()

    user_input = st.chat_input("Converse com Gary Halbert")

    if user_input:
        with st.chat_message("human"):
            st.write(user_input)
            
        with st.chat_message("ai", avatar="files/imgs/Gary-Halbert.jpg"):
            response = []
            response_stream = garyhalbert_agent.run(user_input, stream=True)
            for event in response_stream:
                if event.event == "RunResponseContent":
                    response.append(event.content)
            st.write_stream(response)

def main():
     chat_page()
    
if __name__ == "__main__":
     main()