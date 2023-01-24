from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, SaleViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('sales', SaleViewSet, basename='sales')
router.register('stock', StockViewSet)
