from rest_framework.serializers import ModelSerializer
from tela.task import notifica_tela
from .models import Processo


class ProcessoSerializer(ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'

    def create(self, validated_data):
        obj = super().create(validated_data)
        if obj:
            serial = ProcessoSerializer(obj)
            notifica_tela(serial)
        return obj
