from concurrent.futures import process
from rest_framework.viewsets import ModelViewSet
from .serializer import ProcessoSerializer
from .models import Processo


class ProcessoView(ModelViewSet):
    serializer_class = ProcessoSerializer
    queryset = Processo.objects.all()
