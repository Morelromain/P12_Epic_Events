from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers

from user import views as users_views
from crm import views as crm_views

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'clients', crm_views.ClientViewSet)
router.register(r'contracts', crm_views.ContractViewSet)
router.register(r'events', crm_views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-secure/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
