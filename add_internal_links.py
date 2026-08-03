# Create the privacy and terms templates
template_privacy = '''{% extends "core/base.html" %}
{% block content %}
<div class="container mt-5 pt-5 pb-5">
    <h1 class="mb-4">Privacy Policy</h1>
    <p>This is a placeholder for the Privacy Policy. This page will be updated with the full legal text soon.</p>
    <a href="/" class="btn-outline-white text-dark mt-3" style="display:inline-block; padding: 10px 20px; border: 1px solid #ccc; text-decoration: none;">Back to Home</a>
</div>
{% endblock %}'''

template_terms = '''{% extends "core/base.html" %}
{% block content %}
<div class="container mt-5 pt-5 pb-5">
    <h1 class="mb-4">Terms of Service</h1>
    <p>This is a placeholder for the Terms of Service. This page will be updated with the full legal text soon.</p>
    <a href="/" class="btn-outline-white text-dark mt-3" style="display:inline-block; padding: 10px 20px; border: 1px solid #ccc; text-decoration: none;">Back to Home</a>
</div>
{% endblock %}'''

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/privacy.html', 'w', encoding='utf-8') as f:
    f.write(template_privacy)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/terms.html', 'w', encoding='utf-8') as f:
    f.write(template_terms)

