from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model="mistral-large-latest")

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
- Keep the summary concise (2-3 sentences).
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

para = input("Give your paragraph: ")

final_prompt = prompt.invoke(
    {
        "paragraph": para
    }
)

response = model.invoke(final_prompt)

print(response.content)