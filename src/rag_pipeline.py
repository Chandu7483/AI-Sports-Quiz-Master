from src.vector_store import VectorStore
from src.web_search import WebSearch
from src.quiz_generator import QuizGenerator


class RAGPipeline:

    def __init__(self):
        self.vector_store = VectorStore()
        self.web_search = WebSearch()
        self.quiz_generator = QuizGenerator()

    def generate_quiz(
        self,
        sport,
        difficulty,
        num_questions,
    ):

        # Retrieve relevant information from ChromaDB
        local_context = self.vector_store.search(
            query=f"""
            {sport}
            {sport} rules
            {sport} famous players
            {sport} tournaments
            {sport} records
            {sport} history
            """,
            n_results=10,
        )

        # Retrieve recent information from the web
        web_context = self.web_search.search(
            query=f"{sport} latest news records tournaments",
            max_results=5,
        )

        # Combine both contexts
        combined_context = []

        if local_context:
            combined_context.extend(local_context)

        if web_context:
            combined_context.extend(web_context)

        context = "\n\n".join(combined_context)

        return self.quiz_generator.generate_quiz(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions,
            context=context,
        )