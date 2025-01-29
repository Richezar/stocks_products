from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet, index

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path("", index, name="index")
]+router.urls
