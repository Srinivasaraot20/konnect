import re

file_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/views.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the import of staff_member_required
content = content.replace("from django.contrib.admin.views.decorators import staff_member_required\n", "")

# Add our custom decorator
custom_decorator = """from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def custom_admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        try:
            # Allow anyone with a profile role to access the dashboard base
            if request.user.profile.role in ['Admin', 'Manager', 'Agent']:
                return view_func(request, *args, **kwargs)
        except Exception:
            pass
        return HttpResponseForbidden("You do not have permission to access the dashboard.")
    return _wrapped_view
"""

if "def custom_admin_required" not in content:
    # Insert right after custom_logout
    content = content.replace("def custom_logout(request):\n    logout(request)\n    return redirect('core:home')\n", "def custom_logout(request):\n    logout(request)\n    return redirect('core:home')\n\n" + custom_decorator)

# Replace all @staff_member_required with @custom_admin_required
content = content.replace("@staff_member_required", "@custom_admin_required")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Decorators updated successfully!")
