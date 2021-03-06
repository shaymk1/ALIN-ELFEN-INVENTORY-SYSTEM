"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', include('store.urls')),
    path('list_items/', include('store.urls')),
    path('add_items/', include('store.urls')),
    # path('receive_new_stock/', include('store.urls')),
    path('update_items/<str:pk>/', include('store.urls')),
    path('delete_items/<str:pk>/', include('store.urls')),
    path('stock_detail/<str:pk>/', include('store.urls')),
    path('issue_items/<str:pk>/', include('store.urls')), 
    path('receive_items/<str:pk>/', include('store.urls')),
    path('reorder_level/<str:pk>/', include('store.urls')),
    path('list_history/', include('store.urls')),
    # path('received_stock/<str:pk>/', include('store.urls')),


]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
