import os
import re

# 1. Remove admin from project urls
proj_urls = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/rekonnect_project/urls.py'
with open(proj_urls, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'from django\.contrib import admin\n', '', content)
content = re.sub(r'from core\.admin import konnect_admin\n', '', content)
content = re.sub(r"path\('admin/', konnect_admin\.urls\),\n?", '', content)
content = re.sub(r"path\('admin/', admin\.site\.urls\),\n?", '', content)

with open(proj_urls, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Add dashboard routes to core urls
core_urls = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/urls.py'
with open(core_urls, 'r', encoding='utf-8') as f:
    core_content = f.read()

new_views = """
    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('dashboard/enquiries/', dashboard_enquiries, name='dashboard_enquiries'),
    path('dashboard/profile/', dashboard_profile, name='dashboard_profile'),
    path('dashboard/settings/', dashboard_settings, name='dashboard_settings'),
    path('api/update-enquiry/<int:id>/', update_enquiry_status, name='update_enquiry_status'),
"""

if 'dashboard_home' not in core_content:
    # Add imports
    import_statement = "from .views import HomeView, submit_enquiry, CustomLoginView, custom_logout, dashboard_home, dashboard_enquiries, dashboard_profile, dashboard_settings, update_enquiry_status\n"
    core_content = re.sub(r'from \.views import .*', import_statement, core_content)
    # Insert paths
    core_content = core_content.replace("urlpatterns = [", "urlpatterns = [\n" + new_views)
    
    with open(core_urls, 'w', encoding='utf-8') as f:
        f.write(core_content)

print("Routes updated successfully!")
