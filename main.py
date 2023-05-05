import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI


def get_text():
    input_text = st.text_area(label="what is your query?", label_visibility='collapsed', placeholder="Your query...", key="text_input")
    return input_text


def fetch_the_relevant_information():
    pass
    # here comes the invocation to the berri.ai for the demo purposes

# st.button("Send", type='secondary', help="Click to query", on_click=fetch_the_relevant_information)


def main():
    # Create a persistent state to store the chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Input field for the user to enter their message
    # user_input = st.text_input("Enter your message:")

    text_input = get_text()

    if len(text_input.split(" ")) > 700:
        st.write("Please enter a shorter query. The maximum length is 700 words.")
        st.stop()
        
    # Button to send the message
    if st.button("Send", type='secondary', help="Click to query"):
        # Append the user's message to the chat history
        st.session_state.chat_history.append(("You", text_input))

        # Simulate a response from the chatbot (you can replace this with your own logic)
        response = "Hello, I am a chatbot. You said: " + text_input
        st.session_state.chat_history.append(("Chatbot", response))

        # Clear the input field
        st.text_input("Enter your message:", value='', key=1)

    # Display the chat history
    for sender, message in st.session_state.chat_history:
        st.write(f"{sender}: {message}")

if __name__ == "__main__":
    main()