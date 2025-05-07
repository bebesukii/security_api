from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from core.application.use_cases import GoogleDorkUseCase

class GoogleDorkSearchView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if not query:
            return Response({"error": "Parámetro 'query' requerido."}, status=status.HTTP_400_BAD_REQUEST)

        use_case = GoogleDorkUseCase()
        results = use_case.execute(query)
        return Response(results, status=status.HTTP_200_OK)
        if not query.strip():
           return Response({"error": "El parámetro 'query' no puede estar vacío."}, status=status.HTTP_400_BAD_REQUEST)


from core.application.use_cases import DNSScanUseCase

class DNSScanView(APIView):
    def get(self, request):
        domain = request.GET.get('domain')
        if not domain:
            return Response({"error": "Parámetro 'domain' requerido."}, status=status.HTTP_400_BAD_REQUEST)

        use_case = DNSScanUseCase()
        result = use_case.execute(domain)
        return Response(result, status=status.HTTP_200_OK)
        if not domain:
            return Response({"error": "Parámetro 'domain' requerido."}, status=status.HTTP_400_BAD_REQUEST)


from core.application.use_cases import ShodanSearchUseCase

class ShodanSearchView(APIView):
    def get(self, request):
        query = request.GET.get('query', 'DVWA')  # Valor por defecto
        use_case = ShodanSearchUseCase()
        results = use_case.execute(query)
        return Response(results, status=status.HTTP_200_OK)
        if not domain:
            return Response({"error": "Parámetro 'domain' requerido."}, status=status.HTTP_400_BAD_REQUEST)

    