# Sentiment-Aware Chatbot  

This is a Streamlit-based chatbot that uses Google's Gemini API to analyze the sentiment of user messages and respond accordingly. The chatbot maintains a history of conversations and provides responses in a friendly, empathetic, or neutral tone based on sentiment analysis.  

## Features  
- Sentiment-aware responses (positive, negative, neutral)  
- Multi-session chat history management  
- Simple and interactive UI using Streamlit  

## Installation  
1. Clone this repository or download the source files.  
2. Install the required dependencies using:  
pip install -r requirements.txt

markdown
Copy code
3. Set up the **GOOGLE_API_KEY** in your environment variables.  

## Usage  
1. Run the chatbot with the following command:  
streamlit run app.py

pgsql
Copy code
2. Use the sidebar to select or start a new chat session.  
3. Enter your message in the text box, and the chatbot will analyze its sentiment and respond accordingly.  

## Requirements  
- Python 3.8+  
- Streamlit  
- Google Generative AI SDK  

## Notes  
- Ensure that you have a valid **Google API Key** for using Gemini AI.  
- This chatbot is designed for demonstration purposes and may require enhancements for production use.  

## License  
This project is licensed under the MIT License.  
