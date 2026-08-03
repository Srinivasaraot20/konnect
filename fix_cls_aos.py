import re

# 1. Fix aos.css in index.html
html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Make aos.css render blocking to prevent CLS
html_content = re.sub(
    r'<link rel="preload" href="https://unpkg\.com/aos@2\.3\.1/dist/aos\.css" as="style" onload="this\.onload=null;this\.rel=\'stylesheet\'">\s*<noscript><link rel="stylesheet" href="https://unpkg\.com/aos@2\.3\.1/dist/aos\.css"></noscript>',
    '<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">',
    html_content
)

# Fix the mobile menu logo style
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Mobile Menu Logo" width="103" height="56" class="mb-4">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Mobile Menu Logo" width="103" height="56" class="mb-4" style="width: 103px; height: 56px; object-fit: contain;">'
)

# Also fix the desktop logos just in case
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48" class="loader-logo mb-3">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48" class="loader-logo mb-3" style="width: 89px; height: 48px; object-fit: contain;">'
)
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48" style="width: 89px; height: 48px; object-fit: contain;">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Fix font-display: optional in style.css
for css_path in ['c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css', 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/staticfiles/style.css']:
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    css_content = css_content.replace('font-display:block;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome', 'font-display:optional;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome')
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

