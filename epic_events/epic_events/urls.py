from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_nested import routers

from user import views as users_views
from crm import views as crm_views


router = routers.DefaultRouter()

router.register(r'users', users_views.UserViewSet)
router.register(r'groups', users_views.GroupViewSet)
router.register(r'clients', crm_views.ClientViewSet)
router.register(r'contracts', crm_views.ContractViewSet)
router.register(r'events', crm_views.EventViewSet)
router.register(r'status', crm_views.StatusViewSet)

router.get_api_root_view().cls.__name__ = "Epic Event"
router.get_api_root_view().cls.__doc__ = (
    "API Epic Event for sales and support user"
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-secure/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
