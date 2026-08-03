import re

html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add circles back
circles = '<div class="position-absolute rounded-circle opacity-10 dec-circle-1 d-none d-md-block"></div>\n      <div class="position-absolute rounded-circle opacity-10 dec-circle-2 d-none d-md-block"></div>\n'

html_content = html_content.replace(
    '<!-- Decorative circles -->\n',
    f'<!-- Decorative circles -->\n      {circles}'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
