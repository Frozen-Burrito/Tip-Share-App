from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('tips/', views.tipList, name="tips"),
    path('get-tip/<str:pk>/', views.getTip, name="get-tip"),
    path('random-tip/', views.randTip, name="random-tip"),

    path('create-tip/', views.createTip, name="create-tip"),
    path('delete-tip/<str:pk>', views.deleteTip, name="delete-tip"),
]