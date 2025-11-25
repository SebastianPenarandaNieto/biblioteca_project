from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register('autores', AutorViewSet)
router.register('libros', LibroViewSet)
router.register('resenas', ResenaViewSet)

urlpatterns = router.urls