with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Google Fonts sync
old_gf = '''<link rel="preload" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap"></noscript>'''
new_gf = '''<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=Montserrat:wght@400;500;600;700&display=swap">'''
html = html.replace(old_gf, new_gf)

# 2. AOS CSS async
old_aos = '''<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">'''
new_aos = '''<link rel="preload" href="https://unpkg.com/aos@2.3.1/dist/aos.css" as="style" onload="this.onload=null;this.rel='stylesheet'">\n  <noscript><link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css"></noscript>'''
html = html.replace(old_aos, new_aos)

# 3. style.css sync
old_style = '''<link rel="preload" href="{% static 'style.css' %}" as="style" onload="this.onload=null;this.rel='stylesheet'">\n  <noscript><link rel="stylesheet" href="{% static 'style.css' %}"></noscript>'''
new_style = '''<link rel="stylesheet" href="{% static 'style.css' %}">'''
html = html.replace(old_style, new_style)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Patched index.html CSS loading')
