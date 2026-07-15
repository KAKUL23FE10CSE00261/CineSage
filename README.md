# 🎬 CineSage - Movie Information Extraction Assistant

CineSage is an AI-powered Movie Information Extraction Assistant built using **LangChain**, **Mistral AI**, and **Streamlit**. It analyzes movie descriptions and automatically extracts important information in a structured and easy-to-read format.

---

## 🚀 Features

- 🎥 Extract Movie Details
  - Movie Name
  - Genre
  - Release Year
  - Language
  - IMDb Rating
  - Duration

- 🎬 Extract Crew Information
  - Director
  - Producer
  - Writer
  - Music Composer
  - Production Company

- ⭐ Extract Cast
  - Lead Actors
  - Supporting Actors

- 📖 Story Information
  - Main Plot
  - Setting
  - Main Theme
  - Conflict
  - Message or Moral

- 🏆 Recognition
  - Awards
  - Achievements

- 🔑 Important Keywords

- 📝 AI Generated Quick Summary

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Python Dotenv

---

## 📂 Project Structure

```
CineSage/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CineSage.git

cd CineSage
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file and add your Mistral API Key.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📥 Input

Paste any movie description or paragraph into the text area.

Example:

> Interstellar is a 2014 science fiction film directed by Christopher Nolan...

---

## 📤 Output

The assistant extracts:

- Movie Details
- Cast & Crew
- Story Information
- Awards
- Important Keywords
- Quick Summary

---

## 📸 Sample Interface

<img width="900" alt="CineSage UI" src="your_screenshot_here"/>

---

## 💡 Future Improvements

- Upload PDF or TXT files
- Movie poster extraction
- JSON export
- Download extracted information
- Multi-language support
- OCR support for movie articles

---

## 👨‍💻 Author

**Kakul Barsaiya**

B.Tech CSE | AI & Machine Learning Enthusiast

---

## ⭐ Support

If you like this project, don't forget to ⭐ the repository.
