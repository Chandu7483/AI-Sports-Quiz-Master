from duckduckgo_search import DDGS


class WebSearch:
    def search(self, query, max_results=5):
        results = []

        with DDGS() as ddgs:
            response = ddgs.text(query, max_results=max_results)

            for item in response:
                results.append(item["body"])

        return results