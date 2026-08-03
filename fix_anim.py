import re

css_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add it back to .gradient-text
css_content = css_content.replace(
    '.gradient-text{background:linear-gradient(135deg,var(--gold),var(--gold-light),var(--gold));background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}',
    '.gradient-text{background:linear-gradient(135deg,var(--gold),var(--gold-light),var(--gold));background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 4s linear infinite;}'
)

# Also check if it's already there
if 'animation:shimmer 4s linear infinite;' not in css_content:
    css_content = css_content.replace(
        'background-clip:text;}',
        'background-clip:text;animation:shimmer 4s linear infinite;}'
    )

# Add keyframes back
if '@keyframes shimmer' not in css_content:
    css_content = css_content.replace(
        '.hero-section{',
        '@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}.hero-section{'
    )

# Just to make sure we also add smooth scroll to html
if 'scroll-behavior: smooth;' not in css_content:
    css_content = css_content.replace(
        'html,body{',
        'html{scroll-behavior:smooth;}html,body{'
    )

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
