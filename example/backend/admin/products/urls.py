from .views import ProductViewSet, UserAPIView
from django.urls import path

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'getAllProducts',
        'post': 'postProduct'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'getProduct',
        'put': 'updateProduct',
        'delete': 'deleteProduct'
    })),
    path('user', UserAPIView.as_view()),
]
