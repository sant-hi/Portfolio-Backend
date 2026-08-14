from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContactMessageAPI


router = DefaultRouter()

router.register(
    "contact",
    ContactMessageAPI,
    basename="contact"
)

urlpatterns = [
    path(
        "",
        include(router.urls)
    ),
]