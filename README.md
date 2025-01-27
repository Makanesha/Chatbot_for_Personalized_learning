
# Personalized Learning Chatbot - MENTORIA

This is a chatbot application built using **Rasa** and **Streamlit**, designed to provide personalized learning recommendations based on user queries. It uses YouTube tutorials as the primary source for educational content, retrieving relevant video recommendations based on the user's selected topic.

## Features
- **Interactive Chatbot**: Users can interact with the chatbot to get educational video suggestions.
- **Personalized Learning**: The bot customizes its suggestions based on the user-provided topic.
- **YouTube Integration**: The bot fetches relevant tutorial videos from YouTube.
- **Streamlit UI**: The chatbot is embedded in a user-friendly interface using Streamlit.

## Technologies Used
- **Rasa**: Open-source conversational AI framework.
- **Streamlit**: Framework to build interactive web applications for machine learning and data science.
- **Google YouTube Data API**: To search and retrieve educational videos from YouTube.
- **Python**: The primary language for backend implementation.

## Setup Instructions

### 1. Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/Chatbot_for_Personalized_learning.git
cd Chatbot_for_Personalized_learning
```

### 2. Install dependencies
Install all the necessary Python libraries by running:
```bash
pip install -r requirements.txt
```

### 3. Set up the YouTube Data API
To set up the YouTube API:
- Go to the [Google Developer Console](https://console.developers.google.com/).
- Create a new project and enable the **YouTube Data API v3**.
- Generate an **API Key** and replace `YOUR_API_KEY` with your actual API key in the `ActionFetchYoutubeVideos` class in the Rasa code. You will find the code for this in the `actions.py` file under your Rasa project directory.

### 4. Set up Rasa
To train the Rasa model:
```bash
rasa train
```

After training, run the Rasa server to enable communication between Rasa and Streamlit:
```bash
rasa run --enable-api
```

If you have custom actions, you need to run the action server in a separate terminal:
```bash
rasa run actions
```

### 5. Set up the Streamlit app
Run the Streamlit app in a separate terminal window:
```bash
streamlit run app.py
```

This will open the Streamlit interface in your browser (`localhost:8501`), where you can interact with the chatbot.

### 6. Chatbot Operation
Once everything is set up and running:
- Open the Streamlit interface in your browser (`localhost:8501`).
- Interact with the chatbot by typing topics related to learning.
- The bot will fetch relevant educational video tutorials from YouTube based on the topic provided.

## Custom Actions
The bot fetches video details using the **YouTube Data API** to provide relevant tutorials. The custom action used for this is the `action_fetch_youtube_videos` class. It works by:
- Searching YouTube for videos based on the user's input (educational-related keywords).
- Filtering the results to get relevant educational content.
- Sorting the videos based on their educational relevance and user engagement (views and likes).

The action ensures that the chatbot provides quality learning content based on the search query.

## Troubleshooting
- **Connection issues**: Ensure that your Rasa server (`rasa run --enable-api`) is running and accessible at `localhost:5005`. This is crucial for the communication between Rasa and Streamlit.
- **API Key issues**: If you face issues with the YouTube API, double-check your API key and ensure it is valid. Make sure it has the correct permissions to access the YouTube Data API v3.
- **Missing dependencies**: If you see errors related to missing libraries, run the following command to install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Contribution
Feel free to fork this repository and submit pull requests for improvements. You can add new features, integrate other platforms, improve the learning recommendation system, or enhance the user interface.

### Ideas for contribution:
- Adding more learning platforms (e.g., Coursera, Udemy).
- Expanding the chatbot's abilities to handle more complex user queries.
- Enhancing the UI/UX of the Streamlit application.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
