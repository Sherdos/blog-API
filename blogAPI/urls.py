"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.posts.views import PostAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView
from apps.users.views import UserAPIView, RegisterAPIView, UpdateAPIView, UserDeleteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', PostAPIView.as_view(), name = "api_posts"),
    path('api/posts/create/', PostCreateAPIView.as_view(), name = "api_post_create"),
    path('api/posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name = "api_posts_update"),
    path('api/posts/delete/<int:pk>/', PostDeleteAPIView.as_view(), name = "api_delete_view"),
    path('api/users/', UserAPIView.as_view(), name = "api_users"),
    path('api/users/register/', RegisterAPIView.as_view(), name = "api_users_register"),
    path('api/users/update/<int:pk>/', UpdateAPIView.as_view(), name='api_users_update'),
    path('api/users/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='api_user_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)