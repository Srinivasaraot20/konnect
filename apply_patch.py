import os
import urllib.request
import base64

# 1. Update settings.py
settings_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/rekonnect_project/settings.py'
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_content = f.read()

if 'WHITENOISE_MAX_AGE = 31536000' not in settings_content:
    settings_content = settings_content.replace(
        "STATIC_ROOT = BASE_DIR / 'staticfiles'",
        "STATIC_ROOT = BASE_DIR / 'staticfiles'\n\n# Long cache lifetime for our own static assets (style.css, main.js, images).\nWHITENOISE_MAX_AGE = 31536000"
    )
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(settings_content)


# 2. Update index.html
html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add preconnects if not there
if 'https://cdn.jsdelivr.net' not in html_content:
    html_content = html_content.replace(
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n  <link rel="preconnect" href="https://cdn.jsdelivr.net" />\n  <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin />\n  <link rel="preconnect" href="https://images.pexels.com" />'
    )

# Remove swiper CSS
import re
html_content = re.sub(r'<!-- Swiper -->.*?swiper-bundle\.min\.css.*?</noscript>', '', html_content, flags=re.DOTALL)
# Remove swiper JS
html_content = re.sub(r'<script src="[^"]*swiper-bundle\.min\.js"[^>]*></script>\s*', '', html_content)

# Font awesome display swap
if '@font-face { font-family:"Font Awesome 6 Free";' not in html_content:
    font_face_css = '''
  <!-- Fix font-display for third-party icon fonts -->
  <style>
    @font-face { font-family:"Font Awesome 6 Free"; font-style:normal; font-weight:900; font-display:swap; src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-solid-900.woff2") format("woff2"); }
    @font-face { font-family:"Font Awesome 6 Free"; font-style:normal; font-weight:400; font-display:swap; src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-regular-400.woff2") format("woff2"); }
    @font-face { font-family:"Font Awesome 6 Brands"; font-style:normal; font-weight:400; font-display:swap; src:url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/webfonts/fa-brands-400.woff2") format("woff2"); }
  </style>
'''
    html_content = html_content.replace(
        '<!-- Performance Preloads -->',
        font_face_css + '\n  <!-- Performance Preloads (URL must match the actual <img> src exactly) -->'
    )

# Preload image w=600 and fetchpriority
html_content = html_content.replace(
    '<link rel="preload" href="https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=700" as="image">',
    '<link rel="preload" href="https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=600" as="image" fetchpriority="high">'
)
# Main image w=600 and fetchpriority
html_content = html_content.replace(
    'width="700" height="380" class="w-100 object-fit-cover" style="height: 380px;">',
    'width="700" height="380" class="w-100 object-fit-cover" style="height: 380px;" fetchpriority="high" decoding="async">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)


# 3. Update main.js
js_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace scroll handler
old_scroll = '''  const scrollHandler = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    
    if (scrollProgress) scrollProgress.style.width = progress + '%';
    
    if (scrollTop > 60) {
      navbar.classList.add('scrolled');
      backToTop.classList.remove('d-none');
    } else {
      navbar.classList.remove('scrolled');
      backToTop.classList.add('d-none');
    }

    // Active link updating
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollY >= sectionTop - 150) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === #) {
        link.classList.add('active');
      }
    });
  };
  window.addEventListener('scroll', scrollHandler, { passive: true });'''

new_scroll = '''  const scrollHandler = () => {
    // --- Reads first (batched) to avoid forced synchronous reflow ---
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;

    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollTop >= sectionTop - 150) {
        current = section.getAttribute('id');
      }
    });

    // --- Writes after all reads ---
    if (scrollProgress) scrollProgress.style.width = progress + '%';

    if (scrollTop > 60) {
      navbar.classList.add('scrolled');
      backToTop.classList.remove('d-none');
    } else {
      navbar.classList.remove('scrolled');
      backToTop.classList.add('d-none');
    }

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === #) {
        link.classList.add('active');
      }
    });
  };

  // Throttle to one run per animation frame so fast scrolling doesn't
  // stack up redundant layout reads/writes.
  let scrollTicking = false;
  window.addEventListener('scroll', () => {
    if (!scrollTicking) {
      requestAnimationFrame(() => {
        scrollHandler();
        scrollTicking = false;
      });
      scrollTicking = true;
    }
  }, { passive: true });'''

if 'scrollTicking' not in js_content:
    js_content = js_content.replace(old_scroll, new_scroll)

# Replace w=600 and w=400 with w=300
js_content = js_content.replace('w=600', 'w=300').replace('w=400', 'w=300')

# Replace desc to description
js_content = js_content.replace("document.getElementById('modalPropertyDesc').innerText = details.desc;", "document.getElementById('modalPropertyDesc').innerText = details.description;")

# Update whatsapp text
old_whatsapp = '''const msg = propertyMessages[title] || 🏡 Hello Konnect Projects,

I'm interested in .

Please share the available options and details.

Thank you.;
        window.open(https://wa.me/919059598777?text=, '_blank');'''

new_whatsapp = '''window.openWhatsApp(title);'''
if 'window.openWhatsApp(title);' not in js_content:
    js_content = js_content.replace(old_whatsapp, new_whatsapp)

# Replace whatsapp messages
js_content = js_content.replace("I'm interested in your Premium Apartments in Hyderabad.", "I'm interested in your Premium Apartments.")
js_content = js_content.replace("✅ Available Apartments\\n✅ 2/3/4 BHK Options\\n✅ Floor Plans\\n✅ Amenities\\n✅ Project Brochure\\n✅ Site Visit\\n✅ Loan Assistance", "✅ Available Apartments\\n✅ 2 BHK / 3 BHK / 4 BHK Options\\n✅ Floor Plans\\n✅ Amenities & Features\\n✅ Project Brochure\\n✅ Site Visit Availability\\n✅ Home Loan Assistance")
js_content = js_content.replace("🌳 Hello", "🌱 Hello")
js_content = js_content.replace("🏠 Hello", "🏡 Hello")


with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# Just copy it to staticfiles as well to be safe
import shutil
shutil.copy2(js_path, 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/staticfiles/main.js')

