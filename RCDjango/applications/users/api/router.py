
from rest_framework.routers import DefaultRouter
from .views import UserApiViewSet

router_user=DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)

