from rest_framework import serializers
from .models import InvestorQuery

class InvestorQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorQuery
        fields = '__all__'
