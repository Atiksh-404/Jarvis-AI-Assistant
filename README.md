# 🤖 Jarvis AI Assistant

A voice-controlled AI desktop assistant built with **Python** and **Google Gemini**.

Jarvis can listen to voice commands, respond using speech, interact with AI, provide information such as weather and news, open websites, play music, and provide a graphical user interface.

---

## 🖥️ Project Preview

![Jarvis AI Assistant](jarvis-preview.png)

## ✨ Features

- 🎤 Voice command recognition
- 🔊 Text-to-speech responses
- 🧠 Google Gemini AI integration
- 🌦️ Weather information
- 📰 Latest news updates
- 🎵 YouTube/music playback
- 🌐 Open websites using voice commands
- 🕐 Current time and date
- 🖥️ Custom graphical user interface
- 🗣️ Wake-word based interaction
- 🔐 Secure API key storage using environment variables

---

## 🛠️ Technologies Used

- **Python**
- **Google Gemini API**
- **SpeechRecognition**
- **PyAudio**
- **pyttsx3**
- **CustomTkinter**
- **Requests**
- **python-dotenv**
- **YouTube Data API**
- **News API**
- **Weather API**

---

## 📁 Project Structure

```text
Jarvis-AI-Assistant/
│
├── assets/
│   └── yesboss.mp3
│
├── modules/
│   ├── __init__.py
│   ├── ai.py
│   ├── news.py
│   ├── time_utils.py
│   ├── weather.py
│   └── youtube.py
│
├── .gitignore
├── generate_voice.py
├── gui.py
├── jarvis_gif.gif
├── main.py
├── requirements.txt
└── README.mds
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Atiksh-404/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant

2. Create a Virtual Environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

4. Configure API Keys

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
WEATHER_API_KEY=your_weather_api_key
YOUTUBE_API_KEY=your_youtube_api_key

Never upload the .env file to GitHub.

5. Run Jarvis
python gui.py
```
