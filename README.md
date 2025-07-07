# 🌌 Nova AI Assistant — A Smart Desktop Voice Assistant

Nova is an intelligent and customizable **AI Voice Assistant** built in **Python** that mimics the behavior of digital assistants like **JARVIS**. It uses voice recognition and natural language processing to respond to user commands and perform a wide variety of desktop and web tasks with ease.

Nova is designed to assist users in their daily activities such as opening applications, searching the web, telling the time/date, and more — all through **hands-free voice commands**.

---

## 🧠 Core Functionalities

Nova is capable of the following tasks:

### 🎙️ Voice Command Recognition
- Captures user speech input using the microphone.
- Converts speech to text using the `SpeechRecognition` library.

### 📢 Text-to-Speech Response
- Converts text-based outputs into audible speech.
- Uses `pyttsx3` for offline TTS (Text-to-Speech).

### 🌐 Web and Internet Tasks
- Opens frequently used websites like Google, YouTube, Gmail, Stack Overflow, etc.
- Can perform Google searches based on voice queries.

### 🖥️ System-level Actions
- Opens system applications such as Notepad, Calculator, File Explorer, or any executable file.
- Retrieves and tells the current system time and date.

### 🛑 Graceful Termination
- Detects exit keywords like "exit", "quit", or "stop" to safely shut down the assistant.

---

## 📌 Use Cases

Here are some example voice commands you can give to Nova:

| Command | Action |
|--------|--------|
| "Open Google" | Launches Google in your default browser |
| "Search for AI in Python" | Performs a Google search |
| "What’s the time?" | Responds with current system time |
| "Open YouTube" | Opens YouTube in your browser |
| "Open Notepad" | Launches the Notepad application |
| "Exit the assistant" | Shuts down Nova safely |



