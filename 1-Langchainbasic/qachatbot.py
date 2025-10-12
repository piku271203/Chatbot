import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

# ---------------------- Page Configuration ----------------------
st.set_page_config(
    page_title="Q&A Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------------- Header ----------------------
st.title("🤖 Q&A Chatbot")
st.caption("Powered by **LangChain** + **Groq** — Get clear, concise, and precise answers.")

# ---------------------- Sidebar ----------------------
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "🔑 Enter Groq API Key", 
        type="password", 
        help="Get a free API key from https://console.groq.com"
    )
    os.environ["GROQ_API_KEY"] = api_key

    model_name = st.selectbox(
        "🧠 Choose Model",
        ["llama-3.1-8b-instant", "llama-3.1-8b", "llama-3.1-8b-chat"],
        index=0
    )

    st.markdown("---")
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------------------- Session Setup ----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------- Model Initialization ----------------------
@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        return None
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0.7,
        streaming=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Answer clearly, precisely, and concisely."),
        ("user", "Question: {question}")
    ])

    return prompt | llm | StrOutputParser()

chain = get_chain(api_key, model_name)

# ---------------------- Chat Section ----------------------
if not chain:
    st.warning("⚠️ Please enter your Groq API Key to start chatting.")
    st.markdown("🔗 [Get your free API key here](https://console.groq.com)")
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ---------------------- Text Input (Above Footer) ----------------------
question = st.chat_input("💬 Type your question...")

if chain and question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

    try:
        for chunk in chain.stream({"question": question}):
            full_response += chunk
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------------------- Suggestions (No Divider Above) ----------------------
st.subheader("💡 Try These Prompts")

col1, col2 = st.columns(2)

with col1:
    st.markdown("- 🌅 Write a short poem about the sunrise over a futuristic city.")
    st.markdown("- 🎨 Describe a world where humans communicate only through colors.")

with col2:
    st.markdown("- 🛸 Imagine an alien visit — what surprises them most about Earth?")
    st.markdown("- 🏔️ Create a dialogue between a river and a mountain debating who is older.")

# ---------------------- Footer ----------------------
st.markdown(
    "<hr style='margin-top: 1.5rem; margin-bottom: 0.5rem;'>"
    "<p style='text-align:center; font-size:14px;'>🧩 Built with ❤️ using <b>LangChain</b> and <b>Groq</b><br>"
    "by <a href='https://github.com/abhijit1901' target='_blank'>Abhijit Jha</a></p>",
    unsafe_allow_html=True
)
