from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet, index

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
