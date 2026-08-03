import re

# 1. Read style.css
with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 2. Remove shimmer animation
css = css.replace('animation:shimmer 4s linear infinite;', '')
css = css.replace('@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}', '')

# 3. Add mobile media query for .hero-bg
old_bg = '''.hero-bg{position:absolute;inset:0;background:url('https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=1920') center/cover no-repeat;background-color:var(--royal-blue-dark);}'''
new_bg = '''.hero-bg{position:absolute;inset:0;background:url('https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=600') center/cover no-repeat;background-color:var(--royal-blue-dark);}
@media (min-width: 768px) {
  .hero-bg{background:url('https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=1920') center/cover no-repeat;background-color:var(--royal-blue-dark);}
}'''
css = css.replace(old_bg, new_bg)

# 4. Update index.html
with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the style.css link and noscript
old_link = '''  <!-- Custom CSS -->
  <link rel="preload" href="{% static 'style.css' %}" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="{% static 'style.css' %}"></noscript>'''

new_style_block = f'''  <!-- Inlined Critical CSS -->
  <style>
    {css}
  </style>'''

html = html.replace(old_link, new_style_block)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully inlined CSS and applied optimizations.')
