"""stoksmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp1 import views
urlpatterns = [
    path('fillanddillsebi/viewall/',views.Fill_SEBI2_list),
    path('fillanddillcash/viewall/',views.FillAndDill_Cash2_list),
    path('fillanddillsebi/',views.FillAndDill_SEBI_list),
    path('fillanddillcash/',views.FillAndDill_Cash_list),
    path('nifty/',views.Nifty_list),
    path('sensex/',views.Sensex_list),
    path('nse/viewall/',views.NSE2_list),
    path('nse/',views.NSE_list),
    path('bse/viewall/',views.BSE2_list),
    path('bse/',views.BSE_list),
    path('globalindices/viewall/',views.GlobalIndices2_list),
    path('globalindices/',views.GlobalIndices_list),
    path('indianindices/viewall/',views.IndianIndices_list2),
    path('indianindices/',views.IndianIndices_list),
    path('admin/', admin.site.urls),
]
