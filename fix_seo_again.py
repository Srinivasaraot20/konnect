import re

html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update Schema
old_schema = '''      {
        "@type": "WebPage",'''
new_schema = '''      {
        "@type": ["WebPage", "Article"],'''
html_content = html_content.replace(old_schema, new_schema)

# 2. Add Internal Links and Last Updated Date to Content
old_summary = '''<p class="hero-text mb-5 text-white-50" style="max-width: 540px;">
              <strong>Bottom-line answer:</strong> As an experienced property investment consultant in Hyderabad with over 15 years of market knowledge, Konnect Projects helps <strong>investors and families</strong> find legally verified, high-appreciation open plots, luxury villas, and commercial spaces across Telangana and AP.
            </p>'''

new_summary = '''<p class="hero-text mb-5 text-white-50" style="max-width: 540px;">
              <strong>Bottom-line answer:</strong> As an experienced property investment consultant in Hyderabad with over 15 years of market knowledge, Konnect Projects helps <strong>investors and families</strong> find legally verified, high-appreciation open plots, luxury villas, and commercial spaces across Telangana and AP.
              <br><br>
              <small><em>Last updated: <time datetime="2026-08-03">August 3, 2026</time> &bull; Learn more in our <a href="/privacy-policy/" class="text-white text-decoration-underline">Privacy Policy</a> and <a href="/terms-of-service/" class="text-white text-decoration-underline">Terms of Service</a>.</em></small>
            </p>'''

html_content = html_content.replace(old_summary, new_summary)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

