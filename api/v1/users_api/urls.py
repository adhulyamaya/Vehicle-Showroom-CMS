from django.urls import path
from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView


app_name = 'users_api'


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', views.login_user, name='login'),
    
    path('users/',views.get_user_profile,name='user_list'),
    path("users/<int:id>/",views.get_user_profile_by_id,name='user-detail'),

    path('admin/create/', views.create_admin_user, name='create_admin_user'),
    path('admin/<int:id>/delete/', views.delete_admin_user, name='delete_admin_user'),
    path('admin/<int:id>/', views.update_admin_user, name='update_admin_user'),
   
]
