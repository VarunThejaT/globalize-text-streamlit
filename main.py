import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.

    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="Sortino", page_icon=":robot:")
st.header("Sortino")

col1, col2 = st.columns(2)
with col1:
    # choose the company - this should be a pretty quick lookup of all the options available
    # for demo purposes, we would have just one drop down
    option_company = st.selectbox( 'Company?', ['Netflix'])
    
with col2:
    st.markdown('Sources:')
    option_dialect = st.radio('News')

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
