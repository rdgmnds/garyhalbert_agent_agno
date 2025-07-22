
import streamlit as st
from agents import *

def chat_page():
    """Cria a pagina do chat"""

    st.set_page_config(
        page_title="IA do Gary Halbert",
        page_icon="✍️",
    )

    st.markdown("# Converse com o maior guru e galã do marketing de resposta direta!")
    st.image("files/imgs/Gary-Halbert.jpg")
    st.markdown("### Você está conversando com um agente de IA treinado com quase todo o conteúdo que Gary publicou em suas cartas.")
    st.divider()

    # cria session para o histórico das mensagens
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # apresenta o histórico de conversas
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
            with st.spinner("Gary está digitando..."):
            # executa o agente e busca apenas o conteúdo da resposta
                response = []
                response_stream = garyhalbert_agent.run(user_input, stream=True)
                for event in response_stream:
                    if event.event == "RunResponseContent":
                        response.append(event.content)
                resposta_final = "".join(response)
                st.write_stream(response)
            
            # adiciona no histórico de conversas
            st.session_state.chat_history.append({
                "role": "ai",
                "avatar": "files/imgs/Gary-Halbert.jpg",
                "type": "text",
                "content": resposta_final
            })

def main():
    # executar esse load apenas na primeira vez (para criar o db de conhecimento)
    #garyhalbert_agent.knowledge.load(recreate=False)
    chat_page()
    
if __name__ == "__main__":
    main()
