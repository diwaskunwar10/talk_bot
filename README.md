
Voice Assistant Powered by Gemini AI

This project demonstrates how to create a voice assistant using the Google Gemini AI for natural language processing, speech recognition, and text-to-speech functionalities. The assistant listens to the user's speech, processes the input with Gemini AI, and provides a spoken response.
Prerequisites

Ensure you have the following installed:

    Python 3.6+
    google-generativeai
    python-dotenv
    speechrecognition
    pyttsx3

You will also need a Google API key to access the Gemini AI services.
Setup

    Clone the repository (if you haven't already):

    sh

git clone <repository-url>
cd <repository-directory>

Create a virtual environment (recommended):

sh

python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install the required packages:

sh

pip install google-generativeai python-dotenv speechrecognition pyttsx3

Set up environment variables:

Create a .env file in the project directory and add your Google API key:

sh

    GOOGLE_API_KEY=your_google_api_key
