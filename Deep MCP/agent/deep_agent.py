from langchain_classic.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from agent.tools import get_person_details, get_all_people
from dotenv import load_dotenv
import os

load_dotenv()

DEEP_SEEK_API=os.getenv("DEEP_SEEK_API")
DEEP_SEEK_URI=os.getenv("DEEP_SEEK_URI")

llm = ChatOpenAI(
    model="deepseek-chat",
    base_url=DEEP_SEEK_URI,
    api_key=DEEP_SEEK_API,
    temperature=0,
    max_retries=3,
    timeout=60,
    request_timeout=60
)


prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant that provide information on ny topic and you can also use tools when needed.
      IMPORTANT: Pay close attention to the conversation history. When the user asks follow-up questions using pronouns like "he", "she", "his", "her", "their", or "it", refer back to the previous messages to understand who or what they're referring to.
                 After you get all the data from the tool, let your reasoning do some logical analysis as asked by user based on data you have got from the tool.

    For example:
    - If the user previously asked about "Ali" and then asks "what is his profession?", you should understand they're asking about Ali's profession.
    - Use the context from previous messages to resolve ambiguous references.
    - If the user refers to a person or object in a follow-up question, use the conversation history to understand who or what they're referring to.
    - Always review the chat history before responding to ensure you understand the full context of the conversation.
    - If user changes the topic, adapt accordingly and accurately.

    Always review the chat history before responding to ensure you understand the full context of the conversation."""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

tools = [get_person_details, get_all_people]

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="output"
)

agent = create_openai_tools_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    return_intermediate_steps=False
)

# user_id = 2cb6e8f0-cca6-4d4e-996f-3f7f2f94f5fa
# batch_id = bb00797c-d1c0-43e7-bbc5-54f57ee963b3