from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductViewSet, StockViewSet, index

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path("", views.index, name="index"),
]+router.urls
