import re

# 1. Fix image sizes in index.html
html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace first loader logo
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="88" height="48" class="loader-logo mb-3" style="height: 48px; width: auto;">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48" class="loader-logo mb-3">'
)
# Replace navbar logo
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="88" height="48" style="height: 48px; width: auto;">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Logo" width="89" height="48">'
)
# Replace mobile menu logos
html_content = html_content.replace(
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Mobile Menu Logo" width="175" height="56" class="mb-4" style="height: 56px; width: auto;">',
    '<img src="{% static \'image.webp\' %}" alt="Konnect Projects Mobile Menu Logo" width="103" height="56" class="mb-4">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)


# 2. Fix font-display: swap to block in style.css to prevent CLS
for css_path in ['c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css', 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/staticfiles/style.css']:
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    css_content = css_content.replace('font-display:swap;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome', 'font-display:block;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome')
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

