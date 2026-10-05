import os

from pinecone import Pinecone
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from langchain_classic.tools.retriever import create_retriever_tool

from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from dotenv import load_dotenv

load_dotenv()


def build_agent() -> AgentExecutor:
    """
    Build Agent only once during application startup.
    """

    # --------------------------------------------------
    # Embedding Model
    # --------------------------------------------------

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        api_key=os.environ["GOOGLE_API_KEY"],
        output_dimensionality=1024
    )

    # --------------------------------------------------
    # Pinecone Connection
    # --------------------------------------------------

    pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )

    index = pc.Index("chatbot-index")

    vector_store = PineconeVectorStore(
        embedding=embeddings,
        index=index
    )

    # --------------------------------------------------
    # Retriever
    # --------------------------------------------------

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name="university_admission_kb",
        description="""
        Search admission policies,
        eligibility criteria,
        fees,
        university rules,
        academic information.
        """
    )

    # --------------------------------------------------
    # LLM
    # --------------------------------------------------

    llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.environ.get("GROQ_API_KEY")
)

    # --------------------------------------------------
    # Agent Prompt
    # --------------------------------------------------

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an Indus University Admission Assistant.

                Your job is to answer questions using ONLY the information
                retrieved from the university knowledge base.

                Rules:
                1. Always use the retrieved documents when answering.
                2. If relevant information is found, provide a complete answer.
                3. Do not ignore retrieved information.
                4. Do not make up information.
                5. Only say "Sorry, I don't have that information."
                   when no relevant information is available in the retrieved documents.
                """
            ),

            MessagesPlaceholder(variable_name="chat_history"),

            ("human", "{input}"),

            MessagesPlaceholder(variable_name="agent_scratchpad")
        ]
    )

    # --------------------------------------------------
    # Agent
    # --------------------------------------------------

    agent = create_tool_calling_agent(
        llm=llm,
        tools=[retriever_tool],
        prompt=prompt
    )

    # --------------------------------------------------
    # Agent Executor
    # --------------------------------------------------

    return AgentExecutor(
        agent=agent,
        tools=[retriever_tool],
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True
    )