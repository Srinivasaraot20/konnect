import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/views.py', 'r', encoding='utf-8') as f:
    views_content = f.read()

# 1. Update submit_enquiry
old_submit = '''@csrf_exempt
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
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)'''

new_submit = '''def submit_enquiry(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            phone = request.POST.get('phone', '').strip()
            location = request.POST.get('location', '').strip()
            propType = request.POST.get('propType', '').strip()
            budget = request.POST.get('budget', '').strip()
            timeline = request.POST.get('timeline', '').strip()
            
            if not all([name, phone, location, propType, budget, timeline]):
                from django.contrib import messages
                messages.error(request, 'Please fill all the required fields.')
                return redirect('/#contact')

            ContactEnquiry.objects.create(
                full_name=name,
                mobile_number=phone,
                email_address=request.POST.get('email', '').strip(),
                preferred_property_type=propType,
                preferred_location=location,
                budget=budget,
                timeline=timeline,
                message=request.POST.get('message', '').strip()
            )
            return redirect('/?success=true#contact')
        except Exception as e:
            from django.contrib import messages
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('/#contact')
    return redirect('/')'''

views_content = views_content.replace(old_submit, new_submit)

# 2. Update dashboard_home stats
old_home_stats = '''    # Calculate stats
    total = ContactEnquiry.objects.count()
    new_enq = ContactEnquiry.objects.filter(status='New').count()
    read_enq = ContactEnquiry.objects.filter(status='Contacted').count()
    closed_enq = ContactEnquiry.objects.filter(status='Closed').count()
    
    latest = ContactEnquiry.objects.order_by('-enquiry_date')[:5]
    
    # Chart Data: Status Pie Chart
    status_data = [new_enq, read_enq, closed_enq]'''

new_home_stats = '''    # Calculate stats
    total = ContactEnquiry.objects.count()
    new_enq = ContactEnquiry.objects.filter(status='New').count()
    contacted_enq = ContactEnquiry.objects.filter(status='Contacted').count()
    followup_enq = ContactEnquiry.objects.filter(status='Follow Up').count()
    interested_enq = ContactEnquiry.objects.filter(status='Interested').count()
    sitevisit_enq = ContactEnquiry.objects.filter(status='Site Visit').count()
    sold_enq = ContactEnquiry.objects.filter(status='Sold').count()
    closed_enq = ContactEnquiry.objects.filter(status='Closed').count()
    
    latest = ContactEnquiry.objects.order_by('-enquiry_date')[:5]
    
    # Chart Data: Status Pie Chart (New, Contacted, Closed)
    status_data = [new_enq, contacted_enq, closed_enq]'''

views_content = views_content.replace(old_home_stats, new_home_stats)

old_home_context = '''        'total_enquiries': total,
        'new_enquiries': new_enq,
        'read_enquiries': read_enq,
        'closed_enquiries': closed_enq,'''

new_home_context = '''        'total_enquiries': total,
        'new_enquiries': new_enq,
        'contacted_enquiries': contacted_enq,
        'followup_enquiries': followup_enq,
        'interested_enquiries': interested_enq,
        'sitevisit_enquiries': sitevisit_enq,
        'sold_enquiries': sold_enq,
        'closed_enquiries': closed_enq,'''

views_content = views_content.replace(old_home_context, new_home_context)

# 3. Add date filter and order by in dashboard_enquiries
old_enq = '''    # Filter
    status_filter = request.GET.get('status', '')
    if status_filter:
        queryset = queryset.filter(status=status_filter)
        
    # Pagination'''

new_enq = '''    # Filter
    status_filter = request.GET.get('status', '')
    if status_filter:
        queryset = queryset.filter(status=status_filter)
        
    date_filter = request.GET.get('date_filter', '')
    today = timezone.now().date()
    if date_filter == 'today':
        queryset = queryset.filter(enquiry_date__date=today)
    elif date_filter == 'yesterday':
        queryset = queryset.filter(enquiry_date__date=today - timedelta(days=1))
    elif date_filter == 'last7':
        queryset = queryset.filter(enquiry_date__date__gte=today - timedelta(days=7))
    elif date_filter == 'last30':
        queryset = queryset.filter(enquiry_date__date__gte=today - timedelta(days=30))
    elif date_filter == 'this_month':
        queryset = queryset.filter(enquiry_date__year=today.year, enquiry_date__month=today.month)
        
    # Pagination'''

views_content = views_content.replace(old_enq, new_enq)

old_enq_context = '''        'search_q': search_q,
        'status_filter': status_filter,
        'active_menu': 'enquiries'
    })'''

new_enq_context = '''        'search_q': search_q,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'active_menu': 'enquiries'
    })'''

views_content = views_content.replace(old_enq_context, new_enq_context)

# 4. Append new views at the end of the file
new_views = '''
from django.shortcuts import get_object_or_404

@login_required
@custom_admin_required
def dashboard_enquiry_detail(request, id):
    context = get_base_context(request)
    enquiry = get_object_or_404(ContactEnquiry, id=id)
    context.update({
        'enquiry': enquiry,
        'active_menu': 'enquiries'
    })
    return render(request, 'dashboard/enquiry_detail.html', context)

@login_required
@custom_admin_required
def dashboard_enquiry_edit(request, id):
    context = get_base_context(request)
    enquiry = get_object_or_404(ContactEnquiry, id=id)
    
    if request.method == 'POST':
        enquiry.full_name = request.POST.get('full_name', enquiry.full_name)
        enquiry.mobile_number = request.POST.get('mobile_number', enquiry.mobile_number)
        enquiry.email_address = request.POST.get('email_address', enquiry.email_address)
        enquiry.preferred_location = request.POST.get('preferred_location', enquiry.preferred_location)
        enquiry.preferred_property_type = request.POST.get('preferred_property_type', enquiry.preferred_property_type)
        enquiry.budget = request.POST.get('budget', enquiry.budget)
        enquiry.timeline = request.POST.get('timeline', enquiry.timeline)
        enquiry.message = request.POST.get('message', enquiry.message)
        enquiry.status = request.POST.get('status', enquiry.status)
        enquiry.admin_notes = request.POST.get('admin_notes', enquiry.admin_notes)
        enquiry.save()
        messages.success(request, 'Enquiry updated successfully.')
        return redirect('core:dashboard_enquiry_detail', id=enquiry.id)
        
    context.update({
        'enquiry': enquiry,
        'active_menu': 'enquiries',
        'status_choices': ContactEnquiry.STATUS_CHOICES
    })
    return render(request, 'dashboard/enquiry_edit.html', context)
'''

views_content += new_views

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/views.py', 'w', encoding='utf-8') as f:
    f.write(views_content)

print('Updated views.py successfully')
