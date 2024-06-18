from rest_framework import serializers
from . models import SkillsModel

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsModel
        fields = '__all__'