
from django.urls import path
from APIView_App import views

urlpatterns = [
    path('emp/', views.EmployeeListView.as_view()),

    path('emp/<int:id>/', views.EmployeeDetailView.as_view())
]
