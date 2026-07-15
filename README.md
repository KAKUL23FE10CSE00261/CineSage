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
git clone https://github.com/KAKUL23FE10CSE00261/CineSage.git

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

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/d3a30c0d-0242-49ef-90bd-d04c768e1c5e" />

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/a9856861-e298-4d53-adb7-672fd3839005" />

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/8abe6f46-1855-4adb-888e-8efb9e769a64" />

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/fd334a07-88a0-4f4f-bee0-bd31f9dc0c7d" />

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/1cdd7e8a-6dbf-4fc9-8e0f-05cc17b1ca6a" />

<img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/07d16ea3-0c46-4deb-8fc7-e611f9e63036" />

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
