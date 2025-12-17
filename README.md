# SentiNL Cyber Defense 🛡️

SentiNL Cyber Defense is a live, AI-powered cybersecurity assistant built to help non-technical users identify, understand, and respond to common digital security threats through an interactive web dashboard.

## 🌐 Live Demo
👉 https://sentinl-cyber-defense.streamlit.app/

---

## 🚀 Features

- **Scam & Phishing Analysis**  
  Analyze suspicious messages and receive AI-generated explanations highlighting red flags, manipulation tactics, and social engineering techniques.

- **Password Strength Checker**  
  Evaluates password security using entropy analysis (`zxcvbn`) and best-practice heuristics to help users create stronger passwords.

- **Data Leak Awareness**  
  Educates users on risks related to exposed credentials and basic data hygiene (no credentials are stored or logged).

- **AI-Powered Explanations**  
  Uses Google GenAI to translate technical cybersecurity risks into clear, human-readable insights.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** (UI & cloud deployment)
- **Google GenAI** (`google-genai`)
- **zxcvbn** (password strength analysis)
- **REST APIs**

---

## 🖥️ Run Locally

```bash
git clone https://github.com/hnaqvi2006/SentiNL-Cyber-Defense.git
cd SentiNL-Cyber-Defense
pip install -r requirements.txt
export GOOGLE_API_KEY="your_api_key_here"
streamlit run app.py

📁 Project Structure

app.py — Main Streamlit application and UI logic

scam_tool.py — Scam and phishing analysis module

pass_tool.py — Password strength evaluation logic

leak_tool.py — Data exposure awareness module

requirements.txt — Project dependencies

🔒 Security & Privacy Notes

API keys are not stored in the repository

Keys are injected via environment variables or Streamlit Secrets

No user input or credential data is persisted or logged

🔮 Future Improvements

MITRE ATT&CK technique mapping for detected threats

URL and domain reputation analysis

Threat intelligence feed integration

User authentication and profiles

📌 Project Status

Live and deployed. Built as a hands-on cybersecurity + AI project demonstrating secure design, debugging, dependency management, and cloud deployment.
