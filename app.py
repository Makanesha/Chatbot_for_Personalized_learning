import streamlit as st
import requests
import time

# Initialize session state variables for storing chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to send user message to the Rasa server and get a response
def get_bot_response(user_input):
    try:
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        headers = {"Content-Type": "application/json"}
        data = {"sender": "user", "message": user_input}

        response = requests.post(rasa_url, json=data, headers=headers)
        if response.status_code == 200:
            bot_responses = response.json()
            if bot_responses:
                # Concatenate all bot responses
                bot_reply = "<br>".join([resp.get("text", "") for resp in bot_responses])
                return bot_reply if bot_reply else "No response"
            else:
                return "No response from the bot."
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Sidebar configuration
with st.sidebar:
    st.header("MENTORIA - Personalized Learning Bot")
    st.header("About MENTORIA")
    st.markdown(
        """
        - **Instructions:** Type your query in the chat box below.
        - **Features:** Mentoria will help you learn your field of interest and guide you in the right path.
        """
    )
    st.header("Features")
    st.markdown(
        """
        - **Ask About:** Know basics about Computer Related terms and gain knowledge about it.
        - **Videos:** Also gives you video materials for your related domains.
        """
    )
    st.info("Dive and Learn for a personalized education experience.")

st.title("Welcome To MENTORIA")

# Initialize chat history in session state if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to fetch model response (both content and video links)
def fetch_model_response(user_input):
    try:
        # Sending the user's query to the Rasa server
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        headers = {"Content-Type": "application/json"}
        data = {"sender": "user", "message": user_input}

        response = requests.post(rasa_url, json=data, headers=headers)
        response.raise_for_status()

        # Extracting response text and video links
        bot_responses = response.json()
        response_text = ""
        video_links = []

        for bot_response in bot_responses:
            if "text" in bot_response:
                response_text += bot_response["text"] + "\n"

            if "attachment" in bot_response and bot_response["attachment"]["type"] == "video":
                video_url = bot_response["attachment"].get("payload", {}).get("url")
                if video_url:
                    video_links.append(video_url)

        return response_text, video_links

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}", []

# Accept user input
if prompt := st.chat_input("Ask a question or type 'bye' to exit."):

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Fetch assistant response from the model (both content and video links)
    with st.spinner('Fetching response from the bot...'):
        response_text, video_links = fetch_model_response(prompt)

    # Display generated content (educational explanation)
    with st.chat_message("assistant"):
        st.markdown(response_text)

    # If video links are found, display them
    if video_links:
        with st.chat_message("assistant"):
            st.markdown("Here are some educational video links you may find useful:")
            for link in video_links:
                st.markdown(f"- [Watch Video]({link})")

    # Add assistant response and video links to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    for link in video_links:
        st.session_state.messages.append({"role": "assistant", "content": f"[Watch Video]({link})"})

# Display chat history
st.markdown("<hr>", unsafe_allow_html=True)

# Add chat history display to show previous messages with styles
chat_display = "".join(st.session_state.chat_history)
st.markdown(chat_display, unsafe_allow_html=True)
