import os

views_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/views.py'
with open(views_path, 'a', encoding='utf-8') as f:
    f.write("""
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
@staff_member_required
def dashboard_home(request):
    pass

@login_required
@staff_member_required
def dashboard_enquiries(request):
    pass

@login_required
@staff_member_required
def dashboard_profile(request):
    pass

@login_required
@staff_member_required
def dashboard_settings(request):
    pass

@login_required
@staff_member_required
def update_enquiry_status(request, id):
    pass
""")

print("Stub views added to views.py!")
