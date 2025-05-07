
class GoogleDorkQuery:
    def __init__(self, query, num_results=5):
        if not query:
            raise ValueError("Query no puede estar vacía.")
        self.query = query
        self.num_results = num_results
