

from django.contrib import admin
from django.urls import path
from transacoes.views import DepositarView, DebitarView
urlpatterns =[ 
    path('admin/', admin.site.urls),
    path("depositar/", DepositarView.as_view(),name="depositar"),
    path("debitar/", DebitarView.as_view(),name="debitar")   
]
