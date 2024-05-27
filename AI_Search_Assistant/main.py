import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.openai import OpenAIChat

st.title("AI Search Assistant")
st.caption("This app allows you to search the web using AI")

openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    assistant = Assistant(
        llm=OpenAIChat(
            model="gpt-4o",
            max_tokens=1024,
            temperature=0.9,
            api_key=openai_access_token,
        ),
        tools=[DuckDuckGo()],
        show_tools_call=True,
    )

    query = st.text_input("Enter the Search Query", type="default")

    if query:
        response = assistant.run(query, stream=False)
        st.write(response)