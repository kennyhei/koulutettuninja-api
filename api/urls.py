from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'general_settings', views.GeneralSettingsViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'contents', views.ContentViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'services', views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
