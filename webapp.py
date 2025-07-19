import streamlit as st
from agents import *

def chat_page():
    st.set_page_config(
        page_title="IA do Gary Halbert",
        page_icon="✍️",
    )

    st.markdown("# Converse com o maior guru e galã do marketing de resposta direta!")
    st.image("files/imgs/Gary-Halbert.jpg")
    st.divider()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            if message["type"] == "text":
                st.write(message["content"])
            elif message["type"] == "stream":
                st.write_stream(message["content"])

    user_input = st.chat_input("Converse com Gary Halbert")

    if user_input:
        st.session_state.chat_history.append({
            "role": "human",
            "avatar": "👤",
            "type": "text",
            "content": user_input
        })

        with st.chat_message("human", avatar="👤"):
            st.write(user_input)

        with st.chat_message("ai", avatar="files/imgs/Gary-Halbert.jpg"):
            response = []

            response_stream = garyhalbert_agent.run(user_input, stream=True)
            for event in response_stream:
                if event.event == "RunResponseContent":
                    response.append(event.content)

            resposta_final = "".join(response)
            st.write_stream(response)

            st.session_state.chat_history.append({
                "role": "ai",
                "avatar": "files/imgs/Gary-Halbert.jpg",
                "type": "text",
                "content": resposta_final
            })


def main():
    chat_page()
    
if __name__ == "__main__":
    main()
