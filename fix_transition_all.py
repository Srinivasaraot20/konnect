import re

css_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

def replacer(match):
    duration = match.group(1)
    return f'transition: transform {duration} ease, opacity {duration} ease, background-color {duration} ease, color {duration} ease, border-color {duration} ease, box-shadow {duration} ease'

css_content = re.sub(r'transition:\s*all\s*([0-9.]+s)(?:\s+ease)?', replacer, css_content)

# Fix Bootstrap's transition all if it's there? No, we don't modify bootstrap min css directly unless needed. The errors point to custom elements (prop-card, btn-gold, etc) which are in style.css.

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# Do the same for staticfiles
css_path2 = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/staticfiles/style.css'
try:
    with open(css_path2, 'w', encoding='utf-8') as f:
        f.write(css_content)
except FileNotFoundError:
    pass
