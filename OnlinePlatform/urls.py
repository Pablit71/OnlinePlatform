"""OnlinePlatform URL Configuration

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
from .yasg import urlpatterns as swagger

from circuit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('all_chain/', views.ChainListView.as_view(), name='all_chain'),
    path('country/', views.InfoChainCountry.as_view(), name='search_country'),
    path('staticdebt/', views.StaticDebt.as_view(), name='debt'),
    path('product/', views.IdProduct.as_view(), name='search_product_id'),
    path('create_chain/', views.CreateChain.as_view(), name='create_chain'),
    path('create_staff/', views.CreateStaff.as_view(), name='create_staff'),
    path('update_chain/<int:pk>', views.UpdateChain.as_view(), name='update_chain/(?P<pk>[0-9]+)\\Z'),
    path('delete_chain/<int:pk>', views.DestroyChain.as_view(), name='delete_chain'),

]

urlpatterns += swagger
