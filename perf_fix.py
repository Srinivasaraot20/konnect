import re

# 1. Fix style.css
css_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace('animation:shimmer 4s linear infinite;', '')
css_content = css_content.replace('@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}', '')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Fix index.html
html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

old_google_fonts = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
new_google_fonts = '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap"></noscript>'
html_content = html_content.replace(old_google_fonts, new_google_fonts)

old_style_css = '<link rel="stylesheet" href="{% static \'style.css\' %}">'
new_style_css = '<link rel="preload" href="{% static \'style.css\' %}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n  <noscript><link rel="stylesheet" href="{% static \'style.css\' %}"></noscript>'
html_content = html_content.replace(old_style_css, new_style_css)

# Font awesome font-display
# We can't change cloudflare font files, but font-awesome usually has swap options.
# Lighthouse says "Font display Est savings of 60 ms" for fa-brands, fa-solid, etc.
# Since we load font-awesome via cdnjs, we can't easily add font-display to it unless we host it ourselves. We will skip this since it's a minor diagnostic issue for external assets.
# But wait, we can append &display=swap to Google Fonts (already there).
# We can resize the image to width="88" height="48"
html_content = html_content.replace(
    '<img src="https://konnect-iota.vercel.app/static/image.webp" alt="Konnect Projects Logo" width="150" height="48" style="height: 48px; width: auto;">',
    '<img src="{% static \'image.png\' %}" alt="Konnect Projects Logo" width="88" height="48" style="height: 48px; width: auto;">'
)
# Wait, the lighthouse report just showed the logo img HTML:
# <img src="/static/image.webp" alt="Konnect Projects Logo" width="150" height="48" style="height: 48px; width: auto;">
# The template might use {% static 'image.png' %}. Let's just fix the width.
html_content = html_content.replace('width="150" height="48"', 'width="88" height="48"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
