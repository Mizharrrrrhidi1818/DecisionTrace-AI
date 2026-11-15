import os

import streamlit as st
from dotenv import load_dotenv

from rag_pipeline import DecisionTraceAI


# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="DecisionTrace AI",
    page_icon="🧠",
    layout="wide"
)

load_dotenv()

st.title("🧠 DecisionTrace AI")
st.caption(
    "AI-Powered Meeting Decision & Commitment Intelligence"
)

st.divider()


# 2. LOAD THE RAG ENGINE
# Cache the model so it doesn't reload on every click.
@st.cache_resource(show_spinner="Loading AI search engine...")
def load_engine():
    return DecisionTraceAI()


# 3. SIDEBAR
with st.sidebar:
    st.header("Project Information")

    st.write("**Project:** DecisionTrace AI")
    st.write("**Technology:** LLM + RAG")
    st.write("**Embedding model:** all-MiniLM-L6-v2")

    st.divider()

    api_key = os.getenv("OPENROUTER_API_KEY", "")
    model_name = os.getenv(
        "OPENROUTER_MODEL",
        "openrouter/free"
    )

    st.subheader("System Status")

    invalid_keys = {
        "",
        "YOUR_ACTUAL_OPENROUTER_API_KEY",
        "paste_your_real_api_key_here"
    }

    key_ready = (
        api_key not in invalid_keys
        and api_key.startswith("sk-or-v1-")
    )

    if key_ready:
        st.success("API key configured")
    else:
        st.warning("OpenRouter API key missing")

    st.caption(f"LLM model: {model_name}")
    st.caption("Runs locally using Streamlit")


# 4. MAIN INTERFACE
st.subheader("Ask About Meeting Decisions")

st.write(
    "Ask a question about NovaTech Solutions "
    "meeting decisions, responsibilities, or deadlines."
)

question = st.text_input(
    "Your question",
    placeholder="Why was the website launch postponed?"
)

ask_button = st.button(
    "Ask DecisionTrace AI",
    type="primary"
)


# 5. RUN RAG PIPELINE
if ask_button:

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            # Initialize retrieval engine
            engine = load_engine()

            if key_ready:
                with st.spinner("Generating AI answer..."):
                    result = engine.ask(question)

                st.subheader("AI-Generated Answer")
                st.write(result["answer"])

                sources = result["sources"]

            else:
                st.warning(
                    "The OpenRouter API key is not configured. "
                    "Showing semantic search results only."
                )

                sources = engine.search_engine.search(
                    question,
                    top_k=5
                )

            # 6. SHOW RETRIEVED EVIDENCE
            st.divider()
            st.subheader("Supporting Evidence")

            for index, source in enumerate(
                sources, start=1
            ):
                with st.expander(
                    f"Evidence {index}: {source['source']}"
                ):
                    st.write(
                        f"**Similarity score:** "
                        f"{source['score']:.4f}"
                    )

                    st.write(source["text"])

        except (ValueError, RuntimeError) as error:
            st.error(str(error))

        except Exception:
            st.error(
                "An unexpected application error occurred. "
                "Check the VS Code terminal for details."
            )


# 7. FOOTER
st.divider()

st.caption(
    "DecisionTrace AI | AI Engineering Portfolio Project"
)