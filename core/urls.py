from django.urls import path
from .views import dashboard_users, user_add, user_edit, user_delete, user_toggle_status, user_reset_password, HomeView, submit_enquiry, CustomLoginView, custom_logout, dashboard_home, dashboard_enquiries, dashboard_profile, dashboard_settings, update_enquiry_status


app_name = 'core'

urlpatterns = [

    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('dashboard/enquiries/', dashboard_enquiries, name='dashboard_enquiries'),
    path('dashboard/profile/', dashboard_profile, name='dashboard_profile'),
    path('dashboard/settings/', dashboard_settings, name='dashboard_settings'),

    path('dashboard/users/', dashboard_users, name='dashboard_users'),
    path('dashboard/users/add/', user_add, name='user_add'),
    path('dashboard/users/<int:id>/edit/', user_edit, name='user_edit'),
    path('dashboard/users/<int:id>/delete/', user_delete, name='user_delete'),
    path('dashboard/users/<int:id>/toggle-status/', user_toggle_status, name='user_toggle_status'),
    path('dashboard/users/<int:id>/reset-password/', user_reset_password, name='user_reset_password'),

    path('api/update-enquiry/<int:id>/', update_enquiry_status, name='update_enquiry_status'),

    path('', HomeView.as_view(), name='home'),
    path('api/submit-enquiry/', submit_enquiry, name='submit_enquiry'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]
