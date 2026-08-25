from django.contrib.auth import views as auth_views
from django.urls import path
from .import views
from .views import (
    root_page, register_view,dashboard_view, profile_view, my_skills_view, add_skill_view,edit_skill_view, delete_skill_view, career_goal_view, skill_gap_view, career_recommendation_view,
)

urlpatterns = [


     path('', root_page, name = 'home'),


    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Registration
    path(
        'register/',
        register_view,
        name='register'
    ),

    # Dashboard
    path(
        'dashboard/',
        dashboard_view,
        name='dashboard'
    ),

    # Profile
    path(
        'profile/',
        profile_view,
        name='profile'
    ),

    #Add Skills
    path(
        'skills/',
        my_skills_view,
        name='my_skills'
    ),

    path(
        'skills/add/',
        add_skill_view,
        name='add_skill'
    ),

    path(
        'skills/edit/<int:skill_id>/',
        edit_skill_view,
        name='edit_skill'
    ),

    path(
        'skills/delete/<int:skill_id>/',
        delete_skill_view,
        name='delete_skill'
    ),

    path(
    'career-goal/',
    career_goal_view,
    name='career_goal'
    ),

    path(
    'skill-gap/',
    views.skill_gap_view,
    name='skill_gap'
    ),

    path(
    'career-recommendation/',
    views.career_recommendation_view,
    name='career_recommendation'
    ),
]


