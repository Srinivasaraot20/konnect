import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove data-aos from hero left column
html = re.sub(r'(<div class="col-lg-6") data-aos="fade-right" data-aos-duration="800">', r'\1>', html)

# 2. Remove data-aos from hero right column
html = re.sub(r'(<div class="col-lg-6 mt-5 mt-lg-0") data-aos="fade-left" data-aos-duration="800">', r'\1>', html)

# 3. Add loading='eager' to hero image
html = html.replace('fetchpriority="high" decoding="async">', 'fetchpriority="high" decoding="async" loading="eager">')

# 4. Add loading='eager' to mobile menu logo
html = html.replace('class="mb-4" style="width: 103px; height: 56px; object-fit: contain;">', 'class="mb-4" style="width: 103px; height: 56px; object-fit: contain;" loading="eager">')

# 5. Fix Bootstrap loading to be synchronous to prevent FOUC / layout shifts
html = html.replace(
    '<link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n  <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"></noscript>',
    '<!-- Bootstrap 5 CSS (Synchronous for LCP/Layout Stability) -->\n  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">'
)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Patched index.html')
