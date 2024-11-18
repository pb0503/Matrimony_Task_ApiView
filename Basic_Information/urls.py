from django.urls import path
from.import views

urlpatterns = [
    path('mv/',views.Member_API.as_view()),
    path('mv/<int:pk>/', views.Member_API.as_view())
]
