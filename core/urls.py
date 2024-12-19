
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('resume/', views.resume_view, name='resume'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),



    # Personal Details
    path('save-personal-details/', views.save_personal_details, name='save_personal_details'),
    path('edit-personal-details/', views.edit_personal_details, name='edit_personal_details'),
    path('delete-personal-details/', views.delete_personal_details, name='delete_personal_details'),
    # Work Experience
    path('add-work/', views.add_work_experience, name='add_work_experience'),
    path('edit-work/<int:pk>/', views.edit_work_experience, name='edit_work_experience'),
    path('delete-work/<int:pk>/', views.delete_work_experience, name='delete_work_experience'),

    # Education
    path('add-education/', views.add_education, name='add_education'),
    path('edit-education/<int:pk>/', views.edit_education, name='edit_education'),
    path('delete-education/<int:pk>/', views.delete_education, name='delete_education'),

    # Skills
    path('add-skill/', views.add_skill, name='add_skill'),
    path('edit-skill/<int:pk>/', views.edit_skill, name='edit_skill'),
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete_skill'),
]
