import csv
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.urls import path
from django.template.response import TemplateResponse
from .models import ContactEnquiry, AdminUserProfile

# Unregister default Group model
admin.site.unregister(Group)

class KonnectAdminSite(admin.AdminSite):
    site_header = 'Konnect Projects Administration'
    site_title = 'Konnect Admin'
    index_title = 'Dashboard'

    def index(self, request, extra_context=None):
        total_enquiries = ContactEnquiry.objects.count()
        new_enquiries = ContactEnquiry.objects.filter(status='New').count()
        read_enquiries = ContactEnquiry.objects.filter(status='Contacted').count() # Using Contacted as Read based on existing choices
        closed_enquiries = ContactEnquiry.objects.filter(status='Closed').count()
        
        latest_enquiries = ContactEnquiry.objects.order_by('-enquiry_date')[:5]

        # Get admin profile pic if exists
        profile_pic_url = None
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            if request.user.profile.profile_image:
                profile_pic_url = request.user.profile.profile_image.url

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': self.get_app_list(request),
            'total_enquiries': total_enquiries,
            'new_enquiries': new_enquiries,
            'read_enquiries': read_enquiries,
            'closed_enquiries': closed_enquiries,
            'latest_enquiries': latest_enquiries,
            'profile_pic_url': profile_pic_url,
            'admin_name': request.user.get_full_name() or request.user.username,
        }
        
        request.current_app = self.name
        return TemplateResponse(request, self.index_template or 'admin/index.html', context)

konnect_admin = KonnectAdminSite(name='konnectadmin')

@admin.action(description='Export selected enquiries to CSV')
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="enquiries.csv"'
    writer = csv.writer(response)
    writer.writerow(['Full Name', 'Mobile Number', 'Email', 'Status', 'Date', 'Message'])
    for enquiry in queryset:
        writer.writerow([
            enquiry.full_name, 
            enquiry.mobile_number, 
            enquiry.email_address, 
            enquiry.status, 
            enquiry.enquiry_date.strftime('%Y-%m-%d %H:%M:%S'),
            enquiry.message
        ])
    return response

class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mobile_number', 'email_address', 'status', 'enquiry_date')
    list_filter = ('status', 'enquiry_date')
    search_fields = ('full_name', 'mobile_number', 'email_address')
    list_editable = ('status',)
    actions = [export_to_csv]

class AdminUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request):
        return False

# Register models to the custom admin site
konnect_admin.register(ContactEnquiry, ContactEnquiryAdmin)
konnect_admin.register(AdminUserProfile, AdminUserProfileAdmin)
# Note: PropertyCategory, PropertyListing, PropertyImage, Testimonial, FAQ are NOT registered here.
