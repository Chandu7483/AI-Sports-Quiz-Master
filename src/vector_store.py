import chromadb

from config import CHROMA_DB_PATH
from src.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

        self.embedding_model = EmbeddingModel()

        self.collection = self.client.get_or_create_collection(
            name="sports_quiz"
        )

        # Load data only once
        if self.collection.count() == 0:

            with open(
                "data/sports_data.txt",
                "r",
                encoding="utf-8"
            ) as file:

                documents = [
                    line.strip()
                    for line in file.readlines()
                    if line.strip()
                ]

            embeddings = self.embedding_model.encode(documents)

            self.collection.add(
                ids=[str(i) for i in range(len(documents))],
                documents=documents,
                embeddings=embeddings,
            )

    def add_documents(self, documents):

        start_id = self.collection.count()

        embeddings = self.embedding_model.encode(documents)

        self.collection.add(
            ids=[
                str(start_id + i)
                for i in range(len(documents))
            ],
            documents=documents,
            embeddings=embeddings,
        )

    def search(self, query, n_results=5):

        query_embedding = self.embedding_model.encode(query)

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results,
        )

        documents = results.get("documents", [])

        if not documents:
            return []

        return documents[0]