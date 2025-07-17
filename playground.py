
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb
from agno.playground import Playground
from mysql_storage_agent import storage
from dotenv import load_dotenv

load_dotenv()

knowledge_base = PDFKnowledgeBase(
    path="files",
    vector_db=ChromaDb(collection="gary_halbert", path="tmp/chromadb", persistent_client=True),
    reader = PDFReader(chunk=True),
)

garyhalbert_agent = Agent(
        name="Gary Halbert",
        model=OpenAIChat(id="gpt-4o"),
        storage=storage,
        knowledge=knowledge_base,
        add_history_to_messages=True,
        read_chat_history=True,
        search_previous_sessions_history=True,
        description=
        '''
        Converse e responda as perguntas como se fosse Gary Halbert, um dos maiores copywriters da hostória.
        Dê preferência a todos os arquivos que te indiquei para responder as perguntas.
        Mantenha o mesmo tom, características, forma de escrever e ironia (humor) que o Gary usa em suas cartas.
        Converse de maneira pessoal, mas sempre responda o que lhe for perguntado.
        Você está em um chat, portanto não precisa se despedir ao final de cada resposta.
        Se você não tiver informações suficientes para responder o que foi perguntado pelo usuário, diga que não sabe.
        Nunca invente informações.
        ''',
    )

playground_app = Playground(agents=[garyhalbert_agent])
app = playground_app.get_app()

if __name__ == "__main__":
    #knowledge_base.load(recreate=True)
    playground_app.serve("playground:app")


