import re

html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Remove the decorative circles entirely to fix the glow issue
html_content = re.sub(r'<div class="position-absolute rounded-circle opacity-10 dec-circle-1"></div>\s*', '', html_content)
html_content = re.sub(r'<div class="position-absolute rounded-circle opacity-10 dec-circle-2"></div>\s*', '', html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
