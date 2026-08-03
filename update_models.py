import os

models_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/models.py'
with open(models_path, 'a', encoding='utf-8') as f:
    f.write("""
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
""")

print("models.py updated successfully!")
