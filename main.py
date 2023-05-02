import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

st.session_state.option_source_news = False

st.set_page_config(page_title="Sortino", page_icon=":robot:")
st.header("Sortino")

col1, col2 = st.columns(2)
with col1:
    # choose the company - this should be a pretty quick lookup of all the options available
    # for demo purposes, we would have just one drop down
    option_company = st.selectbox( 'Company?', ['Netflix'])
    
with col2:
    # choose the source 
    st.markdown('Source:')
    # option_source = st.radio('Sources:', ['News'])
    st.checkbox('News', key="option_source_news")
    # st.checkbox('News', key="option_source_news")

def get_text():
    input_text = st.text_area(label="what is your query?", label_visibility='collapsed', placeholder="Your query...", key="text_input")
    return input_text

text_input = get_text()

if len(text_input.split(" ")) > 700:
    st.write("Please enter a shorter query. The maximum length is 700 words.")
    st.stop()

def fetch_the_relevant_information():
    pass
    # here comes the invocation to the berri.ai for the demo purposes

st.button("Send", type='secondary', help="Click to query", on_click=fetch_the_relevant_information)
