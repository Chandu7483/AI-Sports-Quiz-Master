import gradio as gr
from src.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

SPORTS = [
    "🏏 Cricket",
    "⚽ Football",
    "🏀 Basketball",
    "🎾 Tennis",
    "🏸 Badminton",
    "🏑 Hockey",
    "🤼 Kabaddi",
    "🏐 Volleyball"
]

DIFFICULTY = [
    "Easy",
    "Medium",
    "Hard"
]

QUESTION_COUNT = [
    5,
    10,
    20
]

quiz_data = []
current_question = 0
score = 0
user_answers = []


def start_quiz(sport, difficulty, question_count):
    global quiz_data
    global current_question
    global score
    global user_answers

    score = 0
    current_question = 0
    user_answers = []

    # Remove emoji from sport name
    sport = sport.split(" ", 1)[1]

    try:
        quiz_data = pipeline.generate_quiz(
            sport=sport,
            difficulty=difficulty,
            num_questions=int(question_count)
        )

    except Exception as e:
        return (
            f"## ❌ Error\n\n{str(e)}",
            gr.update(choices=[], value=None, visible=False),
            "",
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False)
        )

    if not quiz_data:
        return (
            "## ❌ No questions were generated.",
            gr.update(choices=[], value=None, visible=False),
            "",
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False)
        )

    question = quiz_data[current_question]

    return (
        f"### Question 1 of {len(quiz_data)}\n\n"
        f"**{question['question']}**",

        gr.update(
            choices=question["options"],
            value=None,
            visible=True
        ),

        "",

        gr.update(visible=False),

        gr.update(visible=True),

        gr.update(visible=False)
    )


def submit_answer(selected_option):
    global current_question
    global score
    global quiz_data
    global user_answers

    if selected_option is None:
        return (
            "⚠️ Please select an answer before submitting.",
            gr.update(visible=False)
        )

    question = quiz_data[current_question]

    user_answers.append(selected_option)

    if selected_option == question["answer"]:
        score += 1

        feedback = f"""
## ✅ Correct!

🎉 Great Job!

### Interesting Fact

{question["interesting_fact"]}
"""

    else:
        feedback = f"""
## ❌ Incorrect!

### Correct Answer

{question["answer"]}

### Explanation

{question["explanation"]}
"""

    return (
        feedback,
        gr.update(visible=True)
    )


def next_question():
    global current_question
    global quiz_data
    global score

    current_question += 1

    if current_question >= len(quiz_data):

        accuracy = (score / len(quiz_data)) * 100

        result = f"""
# 🏆 Quiz Completed!

### Final Score: {score}/{len(quiz_data)}

### Accuracy: {accuracy:.1f}%
"""

        return (
            result,

            gr.update(
                choices=[],
                value=None,
                visible=False
            ),

            "",

            gr.update(visible=False),

            gr.update(visible=False),

            gr.update(visible=True)
        )

    question = quiz_data[current_question]

    return (
        f"### Question {current_question + 1} of {len(quiz_data)}\n\n"
        f"**{question['question']}**",

        gr.update(
            choices=question["options"],
            value=None,
            visible=True
        ),

        "",

        gr.update(visible=True),

        gr.update(visible=False),

        gr.update(visible=False)
    )
with gr.Blocks(title="AI Sports Quiz Master") as demo:

    gr.Markdown("# 🏆 AI Sports Quiz Master")
    gr.Markdown("### Test Your Sports Knowledge with AI")

    with gr.Row():

        sport_dropdown = gr.Dropdown(
            choices=SPORTS,
            value="🏏 Cricket",
            label="Select Sport"
        )

        difficulty_dropdown = gr.Dropdown(
            choices=DIFFICULTY,
            value="Easy",
            label="Difficulty"
        )

        question_dropdown = gr.Dropdown(
            choices=QUESTION_COUNT,
            value=5,
            label="Number of Questions"
        )

    start_button = gr.Button(
        "🚀 Start Quiz",
        variant="primary"
    )

    question_box = gr.Markdown()

    answer_radio = gr.Radio(
        choices=[],
        value=None,
        label="Choose your answer",
        visible=True
    )

    submit_button = gr.Button(
        "Submit Answer",
        visible=True
    )

    feedback_box = gr.Markdown()

    next_button = gr.Button(
        "Next Question",
        visible=False
    )

    restart_button = gr.Button(
        "Restart Quiz",
        visible=False
    )

    start_button.click(
        fn=start_quiz,
        inputs=[
            sport_dropdown,
            difficulty_dropdown,
            question_dropdown
        ],
        outputs=[
            question_box,
            answer_radio,
            feedback_box,
            restart_button,
            submit_button,
            next_button
        ]
    )

    submit_button.click(
        fn=submit_answer,
        inputs=[
            answer_radio
        ],
        outputs=[
            feedback_box,
            next_button
        ]
    )

    next_button.click(
        fn=next_question,
        inputs=[],
        outputs=[
            question_box,
            answer_radio,
            feedback_box,
            submit_button,
            next_button,
            restart_button
        ]
    )

    restart_button.click(
        fn=lambda: (
            "",
            gr.update(
                choices=[],
                value=None,
                visible=True
            ),
            "",
            gr.update(visible=False),
            gr.update(visible=True),
            gr.update(visible=False)
        ),
        outputs=[
            question_box,
            answer_radio,
            feedback_box,
            restart_button,
            submit_button,
            next_button
        ]
    )


if __name__ == "__main__":
    demo.launch()