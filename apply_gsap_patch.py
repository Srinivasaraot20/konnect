import re

html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Remove the inline <style> block for Font Awesome
html_content = re.sub(r'\s*<!-- Fix font-display for third-party icon fonts -->\s*<style>\s*@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}\s*</style>', '', html_content)
html_content = re.sub(r'\s*<!-- Fix font-display for third-party icon fonts \(text stays visible while fonts load\) -->\s*<style>\s*@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}\s*</style>', '', html_content)

# 2. Remove GSAP script
html_content = re.sub(r'\s*<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/[^>]*></script>', '', html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 3. Append to style.css and staticfiles/style.css
css_append = '''
/* font-display:swap override for Font Awesome (loaded async via style.css, so it never competes with the LCP image on the critical path) */
@font-face{font-family:"Font Awesome 6 Free";font-style:normal;font-weight:900;font-display:swap;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.woff2") format("woff2");}
@font-face{font-family:"Font Awesome 6 Free";font-style:normal;font-weight:400;font-display:swap;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-regular-400.woff2") format("woff2");}
@font-face{font-family:"Font Awesome 6 Brands";font-style:normal;font-weight:400;font-display:swap;src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.woff2") format("woff2");}
'''

for css_file in ['c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css', 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/staticfiles/style.css']:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(css_append)

