from django.urls import path

from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.all_projects, name='all_projects'),
    path('contacts/', views.contacts, name='contacts'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    # path('', TemplateView.as_view(template_name="home/home.html")),
]
