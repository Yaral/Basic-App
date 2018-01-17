from django.urls import path

from . import views #added as part of the project

urlpatterns = [
    # ex: /products/
    path('', views.index, name='index'), #added as part of the project
    # ex: /products/5/
    path('<int:product_id>/', views.detail, name='detail') #added as part of the project
]
