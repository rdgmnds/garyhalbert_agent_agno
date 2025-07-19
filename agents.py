
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from dotenv import load_dotenv

load_dotenv()

knowledge_base = PDFKnowledgeBase(
    path="files/pdfs",
    vector_db=ChromaDb(collection="gary_halbert", path="tmp/chromadb", persistent_client=True),
    reader = PDFReader(chunk=True),
)

garyhalbert_agent = Agent(
        name="Gary Halbert",
        model=OpenAIChat(id="gpt-4o"),
        storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db"),
        memory=Memory(model = OpenAIChat(id="gpt-4o"), db = SqliteMemoryDb(table_name="user_memories", db_file="tmp/agent.db")),
        enable_agentic_memory=True,
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
        Saiba que Gary Halbert morreu em 2008.
        ''',
    )


