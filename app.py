import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="CineSage - Movie Information Extraction Assistant",
    page_icon="🎬",
    layout="centered"
)

# ------------------ Load Model ------------------
model = ChatMistralAI(
    model="mistral-large-latest"
)

# ------------------ Prompt ------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Information Extraction Assistant.

Your task is to carefully read the given paragraph and extract all the important information in a clear and organized format.

Instructions:
- Extract only the information that is explicitly mentioned in the paragraph.
- Do not make assumptions or generate missing information.
- If any information is unavailable, write "Not Mentioned".
- Keep the summary concise (2–3 sentences).
- Present the output in a neat, readable format.

Extract the following information:

📌 Movie Details
- Movie Name
- Genre
- Release Year
- Language
- IMDb Rating
- Duration (if mentioned)

🎬 Crew
- Director
- Producer
- Writer
- Music Composer
- Production Company

⭐ Cast
- Lead Actors
- Supporting Actors

📖 Story Information
- Main Plot
- Setting
- Main Theme
- Conflict
- Message or Moral (if mentioned)

🏆 Recognition
- Awards
- Achievements

🔑 Important Keywords

📝 Quick Summary

Make the response well formatted with proper headings and bullet points.
"""
        ),
        (
            "human",
            """
Paragraph:
{paragraph}
"""
        )
    ]
)

# ------------------ UI ------------------
st.title("🎬 CineSage")
st.subheader("Movie Information Extraction Assistant")

st.markdown("""
Welcome to **CineSage**, an AI-powered movie information extraction assistant.

Simply paste a movie description or paragraph below, and CineSage will automatically extract:

- 🎥 Movie Details
- 🎭 Cast & Crew
- 📖 Story Information
- 🏆 Awards & Recognition
- 🔑 Important Keywords
- 📝 Quick Summary
""")

paragraph = st.text_area(
    label="📄 Enter Movie Paragraph",
    height=250,
    placeholder="Paste your movie paragraph here..."
)

if st.button("🎬 Extract Movie Information", use_container_width=True):

    if paragraph.strip() == "":
        st.warning("⚠️ Please enter a movie paragraph.")
    else:
        with st.spinner("🔍 Analyzing movie information..."):

            final_prompt = prompt.invoke(
                {
                    "paragraph": paragraph
                }
            )

            response = model.invoke(final_prompt)

        st.success("✅ Information extracted successfully!")

        st.subheader("📋 Extracted Movie Information")
        st.markdown(response.content)