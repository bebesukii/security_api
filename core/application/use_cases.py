# -*- coding: utf-8 -*-

from core.infrastructure.google_services import GoogleDorkService

class GoogleDorkUseCase:
   def __init__(self, service=None):
        self.service = service or GoogleDorkService()

   def execute(self, query, num_results=5):
        if not query.strip():
            raise ValueError("El parámetro 'query' no puede estar vacío.")
        return self.service.search(query, num_results)



