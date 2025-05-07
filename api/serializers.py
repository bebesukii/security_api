from rest_framework import serializers
from core.domain.models import ScanResult  # Asegúrate de que el modelo exista

class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = ['id', 'domain', 'scan_type', 'result', 'created_at']