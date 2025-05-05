from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('tasks/', views.view_all_tasks, name='task_list'),
    path('task/<int:pk>/update_status/', views.update_task_status, name='update_task_status'),
    path('task/<int:pk>/', views.view_details, name='task_detail'),
    path('task/new/', views.create_task, name='task_create'),
    path('task/<int:pk>/edit/', views.update_task, name='task_update'),
    path('task/<int:pk>/delete/',views.delete_task, name='task_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
     path('api/todos/', views.TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('api/todos/<int:pk>/', views.view_details, name='task_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)