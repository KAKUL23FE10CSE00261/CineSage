# 🎬 CineSage - AI Movie Information Extraction Assistant

CineSage is an AI-powered Movie Information Extraction Assistant built with **LangChain**, **Mistral AI**, and **Streamlit**. It analyzes movie descriptions and automatically extracts structured information such as movie details, cast, crew, plot, awards, keywords, and a concise summary.

## 🌐 Live Demo

🚀 **Try CineSage Here:**  
https://ai-ml-journe-2k7gnqtxreuyidgynmlwro.streamlit.app/

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

- 📖 Story Analysis
  - Main Plot
  - Setting
  - Theme
  - Conflict
  - Message or Moral

- 🏆 Recognition
  - Awards
  - Achievements

- 🔑 Important Keywords

- 📝 AI-Generated Quick Summary

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Python Dotenv

---

## 📂 Project Structure

```text
CineSage/
│── app.py                  # Streamlit user interface
│── core.py                 # LangChain prompt and Mistral AI processing logic
│── requirements.txt        # Project dependencies
│── .env                    # Environment variables (API keys)
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/KAKUL23FE10CSE00261/CineSage.git
cd CineSage
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or using **uv**

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📥 Input

Paste any movie description into the text area.

Example:

> Interstellar is a 2014 science fiction film directed by Christopher Nolan starring Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine...

---

## 📤 Output

CineSage extracts:

- 🎥 Movie Details
- 🎬 Cast & Crew
- 📖 Story Information
- 🏆 Awards & Recognition
- 🔑 Important Keywords
- 📝 AI-Generated Summary

---

## 📸 Application Preview

### Home Screen

<img width="960" alt="Home" src="https://github.com/user-attachments/assets/d3a30c0d-0242-49ef-90bd-d04c768e1c5e"/>

### Sample Input

<img width="960" alt="Input" src="https://github.com/user-attachments/assets/a9856861-e298-4d53-adb7-672fd3839005"/>

### Information Extraction

<img width="960" alt="Extraction" src="https://github.com/user-attachments/assets/8abe6f46-1855-4adb-888e-8efb9e769a64"/>

### Movie Details

<img width="960" alt="Movie Details" src="https://github.com/user-attachments/assets/fd334a07-88a0-4f4f-bee0-bd31f9dc0c7d"/>

### Story Information

<img width="960" alt="Story" src="https://github.com/user-attachments/assets/1cdd7e8a-6dbf-4fc9-8e0f-05cc17b1ca6a"/>

### Summary

<img width="960" alt="Summary" src="https://github.com/user-attachments/assets/07d16ea3-0c46-4deb-8fc7-e611f9e63036"/>

---

## 💡 Future Enhancements

- 📄 Upload PDF or TXT files
- 🎬 Movie poster extraction
- 📥 Export extracted information as PDF or JSON
- 🌍 Multi-language support
- 🖼️ OCR support for scanned movie articles
- 🎤 Voice-based movie description input

---

## 👨‍💻 Author

**Kakul Barsaiya**

B.Tech Computer Science Engineering  
AI & Machine Learning Enthusiast

- GitHub: https://github.com/KAKUL23FE10CSE00261
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support helps improve the project and motivates future development.

---

**Built with ❤️ using LangChain, Mistral AI, and Streamlit.**
