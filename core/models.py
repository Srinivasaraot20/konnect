from django.db import models
from django.contrib.auth.models import User

class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/')
    display_order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Property Categories"
        ordering = ['display_order']

    def __str__(self):
        return self.name

class PropertyListing(models.Model):
    PROPERTY_TYPES = (
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Commercial', 'Commercial'),
        ('Plot', 'Plot'),
        ('Independent House', 'Independent House'),
    )
    
    PROPERTY_STATUS = (
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved'),
    )

    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    category = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True, related_name='properties')
    description = models.TextField()
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField()
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    area = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=PROPERTY_STATUS, default='Available')
    featured = models.BooleanField(default=False)
    amenities = models.TextField(help_text="Comma separated amenities")
    google_map_location = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(PropertyListing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    featured_image = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.property.title} - Image"

class ContactEnquiry(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Closed', 'Closed'),
    )

    full_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    preferred_property_type = models.CharField(max_length=50, blank=True, null=True)
    preferred_location = models.CharField(max_length=100, blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    timeline = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    enquiry_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    # New Fields
    company_name = models.CharField(max_length=150, blank=True, null=True)
    preferred_contact_method = models.CharField(max_length=50, blank=True, null=True)
    preferred_contact_time = models.CharField(max_length=50, blank=True, null=True)
    service_interested_in = models.CharField(max_length=100, blank=True, null=True)
    property_category = models.CharField(max_length=100, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, default='Website', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):
        return f"Enquiry from {self.full_name}"

class AdminUserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Agent', 'Agent'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Agent')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return f"Testimonial from {self.name}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question

class WebsiteSettings(models.Model):
    website_name = models.CharField(max_length=100, default='Konnect Projects')
    admin_email = models.EmailField(default='admin@konnectprojects.com')
    contact_number = models.CharField(max_length=20, default='9059598777')
    whatsapp_number = models.CharField(max_length=20, default='9059598777')
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    def __str__(self):
        return self.website_name
    
    class Meta:
        verbose_name_plural = "Website Settings"
