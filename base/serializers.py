from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import HomeBages

class HomeBagesSerializers(serializers.Serializer):
    model_3d = serializers.SerializerMethodField('get_model_3d')

    class Meta:
        model=HomeBages
        field=['model_3d', 'logo']

    def get_model_3d(self, instance):
        return instance.model_3d.data