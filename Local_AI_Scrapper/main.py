# import the required libraries
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

# set up the Streamlit app
st.title("Web Scrapping AI Agent")

# set up the configuration for the SmartScraperGraph
graph_config = {
    "llm": {
        "model": "ollama/llama3",
        "temperature": 0,
        "format": "json",  # ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set ollama url
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

# get the url of the website to scrape
url = st.text_input("Enter the URL of the website you want to scrape")

# get the user prompt
user_prompt = st.text_input("What you want the AI agent to scrape from the website?")

# create a SmartScraperGraph object
smart_scraper_graph = SmartScraperGraph(
    prompt=user_prompt, source=url, config=graph_config
)

# scrape the website
if st.button("Scrape"):
    result = smart_scraper_graph.run()
    st.write(result)
