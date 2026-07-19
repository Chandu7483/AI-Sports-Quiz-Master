import json
import google.generativeai as genai

from config import GOOGLE_API_KEY, MODEL_NAME
from src.prompt_template import SYSTEM_PROMPT


class QuizGenerator:

    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate_quiz(
        self,
        sport,
        difficulty,
        num_questions,
        context,
    ):

        prompt = f"""
{SYSTEM_PROMPT}

Selected Sport:
{sport}

Selected Difficulty:
{difficulty}

Number of Questions:
{num_questions}

Retrieved Context:
{context}

Generate EXACTLY {num_questions} questions.

Remember:

- Questions must be ONLY about {sport}
- Difficulty must be {difficulty}
- Use Retrieved Context first.
- If necessary, use your sports knowledge ONLY for {sport}.
- Return ONLY valid JSON.
"""

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        # Remove Markdown code blocks if present
        if text.startswith("```json"):
            text = text.replace("```json", "", 1).strip()

        if text.startswith("```"):
            text = text.replace("```", "", 1).strip()

        if text.endswith("```"):
            text = text[:-3].strip()

        try:
            quiz = json.loads(text)

            if not isinstance(quiz, list):
                raise ValueError("Response is not a JSON list.")

            if len(quiz) != num_questions:
                raise ValueError(
                    f"Expected {num_questions} questions but got {len(quiz)}."
                )

            return quiz

        except Exception as e:
            raise Exception(
                f"Failed to parse Gemini response.\n\n"
                f"Error: {e}\n\n"
                f"Raw Response:\n{text}"
            )