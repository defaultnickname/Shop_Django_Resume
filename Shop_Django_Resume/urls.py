"""Shop_Django_Resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from theshop import views as theshop_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', theshop_views.index, name='index'),
    path('cart/', theshop_views.cart, name='cart'),
    path('clothes/', theshop_views.clothes, name='clothes'),
    path('shoes/', theshop_views.shoes, name='shoes'),
    path('accesories/', theshop_views.accesories, name='accesories'),
    path('discount/', theshop_views.discount, name='discount'),
    path('newstuff/', theshop_views.newstuff, name='newstuff'),
    path('admin/', admin.site.urls),
    path('sport/', theshop_views.sport, name='sport'),
    path('products/', theshop_views.products, name='products'),
    path('checkout/', theshop_views.checkout, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)