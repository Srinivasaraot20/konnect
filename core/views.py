from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import (
    PropertyCategory, PropertyListing, Testimonial, FAQ, ContactEnquiry
)

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PropertyCategory.objects.filter(active=True)
        # Assuming we want all featured or all properties. For now just fetch featured.
        context['properties'] = PropertyListing.objects.filter(featured=True).prefetch_related('images')
        context['testimonials'] = Testimonial.objects.all()
        context['faqs'] = FAQ.objects.all()
        return context

@csrf_exempt
def submit_enquiry(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            enquiry = ContactEnquiry.objects.create(
                full_name=data.get('name'),
                mobile_number=data.get('phone'),
                email_address=data.get('email', ''),
                preferred_property_type=data.get('propType', ''),
                preferred_location=data.get('location', ''),
                budget=data.get('budget', ''),
                timeline=data.get('timeline', ''),
                message=data.get('message', '')
            )
            return JsonResponse({'status': 'success', 'message': 'Enquiry saved successfully.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

class CustomLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:dashboard_home')
        return render(request, 'core/login.html')

    def post(self, request):
        email_or_username = request.POST.get('email', '')
        password = request.POST.get('password')
        
        from django.contrib.auth.models import User
        
        # Try to find user by email first
        try:
            user_obj = User.objects.get(email=email_or_username)
            auth_username = user_obj.username
        except User.DoesNotExist:
            auth_username = email_or_username
        except User.MultipleObjectsReturned:
            auth_username = User.objects.filter(email=email_or_username).first().username
            
        # We attempt to authenticate.
        user = authenticate(request, username=auth_username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:dashboard_home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'core/login.html', {'error': 'Invalid login credentials.'})

def custom_logout(request):
    logout(request)
    return redirect('core:home')

from django.core.exceptions import PermissionDenied
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


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.db.models.functions import TruncMonth

from .models import WebsiteSettings, AdminUserProfile

def get_base_context(request):
    try:
        settings_obj = WebsiteSettings.objects.first()
        if not settings_obj:
            settings_obj = WebsiteSettings.objects.create()
    except:
        settings_obj = None
        
    profile = None
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except:
            profile = AdminUserProfile.objects.create(user=request.user)
            
    return {
        'settings': settings_obj,
        'profile': profile,
        'current_user': request.user
    }

@login_required
@custom_admin_required
def dashboard_home(request):
    context = get_base_context(request)
    
    # Calculate stats
    total = ContactEnquiry.objects.count()
    new_enq = ContactEnquiry.objects.filter(status='New').count()
    read_enq = ContactEnquiry.objects.filter(status='Contacted').count()
    closed_enq = ContactEnquiry.objects.filter(status='Closed').count()
    
    latest = ContactEnquiry.objects.order_by('-enquiry_date')[:5]
    
    # Chart Data: Status Pie Chart
    status_data = [new_enq, read_enq, closed_enq]
    
    # Chart Data: Monthly Bar Chart (last 6 months)
    six_months_ago = timezone.now() - timedelta(days=180)
    monthly_data = ContactEnquiry.objects.filter(enquiry_date__gte=six_months_ago) \
        .annotate(month=TruncMonth('enquiry_date')) \
        .values('month') \
        .annotate(count=Count('id')) \
        .order_by('month')
        
    labels = []
    counts = []
    for entry in monthly_data:
        labels.append(entry['month'].strftime('%b %Y'))
        counts.append(entry['count'])
        
    context.update({
        'total_enquiries': total,
        'new_enquiries': new_enq,
        'read_enquiries': read_enq,
        'closed_enquiries': closed_enq,
        'latest_enquiries': latest,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(counts),
        'status_data': json.dumps(status_data),
        'active_menu': 'home'
    })
    
    return render(request, 'dashboard/home.html', context)

@login_required
@custom_admin_required
def dashboard_enquiries(request):
    context = get_base_context(request)
    
    queryset = ContactEnquiry.objects.all().order_by('-enquiry_date')
    
    # Search
    search_q = request.GET.get('search', '')
    if search_q:
        queryset = queryset.filter(full_name__icontains=search_q) | \
                   queryset.filter(email_address__icontains=search_q) | \
                   queryset.filter(mobile_number__icontains=search_q)
                   
    # Filter
    status_filter = request.GET.get('status', '')
    if status_filter:
        queryset = queryset.filter(status=status_filter)
        
    # Pagination
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context.update({
        'page_obj': page_obj,
        'search_q': search_q,
        'status_filter': status_filter,
        'active_menu': 'enquiries'
    })
    
    return render(request, 'dashboard/enquiries.html', context)

@login_required
@custom_admin_required
def dashboard_profile(request):
    context = get_base_context(request)
    context['active_menu'] = 'profile'
    
    if request.method == 'POST':
        user = request.user
        profile = context['profile']
        
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
        profile.save()
        
        # Change password logic could go here, but for simplicity we rely on standard views or custom handling
        new_password = request.POST.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.save()
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, user)
            
        messages.success(request, 'Profile updated successfully!')
        return redirect('core:dashboard_profile')
        
    return render(request, 'dashboard/profile.html', context)

@login_required
@custom_admin_required
def dashboard_settings(request):
    context = get_base_context(request)
    context['active_menu'] = 'settings'
    
    if request.method == 'POST':
        settings_obj = context['settings']
        
        settings_obj.website_name = request.POST.get('website_name', settings_obj.website_name)
        settings_obj.admin_email = request.POST.get('admin_email', settings_obj.admin_email)
        settings_obj.contact_number = request.POST.get('contact_number', settings_obj.contact_number)
        settings_obj.whatsapp_number = request.POST.get('whatsapp_number', settings_obj.whatsapp_number)
        
        if 'logo' in request.FILES:
            settings_obj.logo = request.FILES['logo']
        if 'favicon' in request.FILES:
            settings_obj.favicon = request.FILES['favicon']
            
        settings_obj.save()
        messages.success(request, 'Website settings updated successfully!')
        return redirect('core:dashboard_settings')
        
    return render(request, 'dashboard/settings.html', context)

@csrf_exempt
@login_required
@custom_admin_required
def update_enquiry_status(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')
            enquiry = ContactEnquiry.objects.get(id=id)
            
            if action == 'mark_read':
                enquiry.status = 'Contacted'
                enquiry.save()
            elif action == 'mark_replied':
                enquiry.status = 'Closed'
                enquiry.save()
            elif action == 'delete':
                enquiry.delete()
                return JsonResponse({'status': 'success', 'message': 'Deleted successfully.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid action.'}, status=400)
                
            return JsonResponse({'status': 'success', 'message': 'Status updated successfully.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
import datetime
from django.contrib.auth.hashers import make_password

@login_required(login_url='/login/')
def dashboard_users(request):
    try:
        if request.user.profile.role != 'Admin':
            return HttpResponseForbidden("Only administrators can access this page.")
    except:
        return HttpResponseForbidden("Only administrators can access this page.")
        
    users = User.objects.all()
    
    # Search
    search = request.GET.get('search', '')
    if search:
        users = users.filter(
            Q(username__icontains=search) | 
            Q(email__icontains=search) | 
            Q(first_name__icontains=search) | 
            Q(last_name__icontains=search)
        )
        
    # Filter
    role = request.GET.get('role', '')
    if role:
        users = users.filter(profile__role=role)
        
    status = request.GET.get('status', '')
    if status == 'active':
        users = users.filter(is_active=True)
    elif status == 'inactive':
        users = users.filter(is_active=False)
        
    # Sort
    sort = request.GET.get('sort', 'newest')
    if sort == 'oldest':
        users = users.order_by('date_joined')
    else:
        users = users.order_by('-date_joined')
        
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Stats
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    inactive_users = total_users - active_users
    this_month = timezone.now().replace(day=1, hour=0, minute=0, second=0)
    new_users = User.objects.filter(date_joined__gte=this_month).count()
    
    context = {
        'page_obj': page_obj,
        'search': search,
        'role_filter': role,
        'status_filter': status,
        'sort_filter': sort,
        'total_users': total_users,
        'active_users': active_users,
        'inactive_users': inactive_users,
        'new_users': new_users,
    }
    return render(request, 'dashboard/users.html', context)


@login_required(login_url='/login/')
def user_add(request):
    if request.method == 'POST':
        try:
            if request.user.profile.role != 'Admin':
                return JsonResponse({'status': 'error', 'message': 'Permission denied'})
                
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            full_name = request.POST.get('full_name', '')
            phone = request.POST.get('phone', '')
            role = request.POST.get('role', 'Agent')
            status = request.POST.get('status') == 'Active'
            profile_image = request.FILES.get('profile_image')
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': 'Username already exists.'})
            if User.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'Email already exists.'})
                
            first_name = full_name.split(' ')[0] if full_name else ''
            last_name = ' '.join(full_name.split(' ')[1:]) if full_name else ''
            
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, is_active=status)
            profile = AdminUserProfile.objects.create(user=user, role=role, phone_number=phone)
            
            if profile_image:
                profile.profile_image = profile_image
                profile.save()
            
            return JsonResponse({
                'status': 'success', 
                'message': 'User added successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'full_name': user.get_full_name(),
                    'email': user.email,
                    'phone': profile.phone_number,
                    'role': profile.role,
                    'is_active': user.is_active,
                    'image_url': profile.profile_image.url if profile.profile_image else ''
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required(login_url='/login/')
def user_edit(request, id):
    if request.method == 'POST':
        try:
            if request.user.profile.role != 'Admin':
                return JsonResponse({'status': 'error', 'message': 'Permission denied'})
                
            user = User.objects.get(id=id)
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            if User.objects.filter(username=username).exclude(id=id).exists():
                return JsonResponse({'status': 'error', 'message': 'Username already exists.'})
            if User.objects.filter(email=email).exclude(id=id).exists():
                return JsonResponse({'status': 'error', 'message': 'Email already exists.'})
                
            user.username = username
            user.email = email
            full_name = request.POST.get('full_name', '')
            user.first_name = full_name.split(' ')[0] if full_name else ''
            user.last_name = ' '.join(full_name.split(' ')[1:]) if full_name else ''
            user.is_active = (request.POST.get('status') == 'Active')
            user.save()
            
            profile, _ = AdminUserProfile.objects.get_or_create(user=user)
            profile.role = request.POST.get('role', 'Agent')
            profile.phone_number = request.POST.get('phone', '')
            
            profile_image = request.FILES.get('profile_image')
            if profile_image:
                profile.profile_image = profile_image
            
            profile.save()
            
            return JsonResponse({
                'status': 'success', 
                'message': 'User updated successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'full_name': user.get_full_name(),
                    'email': user.email,
                    'phone': profile.phone_number,
                    'role': profile.role,
                    'is_active': user.is_active,
                    'image_url': profile.profile_image.url if profile.profile_image else ''
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required(login_url='/login/')
def user_delete(request, id):
    if request.method == 'POST':
        try:
            if request.user.profile.role != 'Admin':
                return JsonResponse({'status': 'error', 'message': 'Permission denied'})
            if request.user.id == id:
                return JsonResponse({'status': 'error', 'message': 'Cannot delete your own account.'})
                
            User.objects.filter(id=id).delete()
            return JsonResponse({'status': 'success', 'message': 'User deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required(login_url='/login/')
def user_toggle_status(request, id):
    if request.method == 'POST':
        try:
            if request.user.profile.role != 'Admin':
                return JsonResponse({'status': 'error', 'message': 'Permission denied'})
            if request.user.id == id:
                return JsonResponse({'status': 'error', 'message': 'Cannot deactivate your own account.'})
                
            user = User.objects.get(id=id)
            user.is_active = not user.is_active
            user.save()
            
            return JsonResponse({'status': 'success', 'is_active': user.is_active, 'message': 'Status updated'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required(login_url='/login/')
def user_reset_password(request, id):
    if request.method == 'POST':
        try:
            if request.user.profile.role != 'Admin':
                return JsonResponse({'status': 'error', 'message': 'Permission denied'})
                
            # Use json for this specific payload or form data
            if request.content_type == 'application/json':
                import json
                data = json.loads(request.body)
                password = data.get('password')
            else:
                password = request.POST.get('password')
                
            if not password:
                return JsonResponse({'status': 'error', 'message': 'Password cannot be empty'})
                
            user = User.objects.get(id=id)
            user.set_password(password)
            user.save()
            
            return JsonResponse({'status': 'success', 'message': 'Password reset successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
