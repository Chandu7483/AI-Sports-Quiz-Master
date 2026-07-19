from src.quiz_generator import QuizGenerator


def test_quiz_generator_creation():
    generator = QuizGenerator()
    assert generator is not None