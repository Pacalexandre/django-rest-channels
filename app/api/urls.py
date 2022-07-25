from rest_framework.routers import DefaultRouter
from .views import ProcessoView

router = DefaultRouter(trailing_slash=False)
router.register('processos', ProcessoView, basename='processo')
