from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, SaleViewSet, StockViewSet


router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('sales', SaleViewSet)
router.register('stock', StockViewSet)
