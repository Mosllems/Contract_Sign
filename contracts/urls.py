from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.create_contract, name="create"),
    path("sign/<int:contract_id>", views.sign_contract, name="sign_contract"),
    path("success/", views.success, name="success"),
    path('sign/<int:contract_id>/second/', views.sign_contract_second, name='sign_contract_second'),
    path("success_second/", views.success, name="success_second"),
]