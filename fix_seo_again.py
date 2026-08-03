import re

html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update Schema
old_schema = '"@type": "RealEstateAgent",'
new_schema = '"@type": ["Organization", "RealEstateAgent", "LocalBusiness"],'
html_content = html_content.replace(old_schema, new_schema)

old_webpage = '"@id": "https://konnectprojects.in/#organization"\n        },'
new_webpage = '"@id": "https://konnectprojects.in/#organization"\n        },\n        "publisher": {"@id": "https://konnectprojects.in/#organization"},'
html_content = html_content.replace(old_webpage, new_webpage)

# 2. Update H1 and hero title
html_content = html_content.replace(
    '<h1 class="hero-title text-white mb-4">\n              Find the Right Property <br>\n              <span class="gradient-text">with Confidence</span>\n            </h1>',
    '<h1 class="hero-title text-white mb-4">\n              Best Real Estate Consultant in Hyderabad: <br>\n              <span class="gradient-text">Find the Right Property</span>\n            </h1>'
)

# 3. Update Executive Summary for AEO/GEO signals
old_summary = '''<h2 class="fw-bold mb-3" style="font-family: 'Poppins'; font-size: 1.5rem; color: var(--royal-blue-dark);">
                Executive Summary: What We Do & Who We Serve
              </h2>
              <p style="color: var(--gray); font-size: 1rem; line-height: 1.8; margin-bottom: 24px;">
                <strong>Konnect Projects</strong> is a leading real estate consultancy helping families, first-time buyers, and seasoned investors secure highly profitable and legally verified properties across Hyderabad, Telangana, and Andhra Pradesh. Whether you are looking for a <a href="#properties" class="text-decoration-none fw-bold" style="color: var(--gold);">luxury villa</a>, a <a href="#properties" class="text-decoration-none fw-bold" style="color: var(--gold);">commercial space</a>, or a <a href="#properties" class="text-decoration-none fw-bold" style="color: var(--gold);">high-growth open plot</a>, our 15+ years of market expertise ensure you make the best financial decision.
              </p>'''

# Wait, in the earlier output, I saw it was "What We Do & Who We Serve", let me double check the exact string
# Let me just use regex for the summary block
new_summary = '''<h2 class="fw-bold mb-3" style="font-family: 'Poppins'; font-size: 1.5rem; color: var(--royal-blue-dark);">
                Key Takeaway Summary
              </h2>
              <p style="color: var(--gray); font-size: 1rem; line-height: 1.8; margin-bottom: 24px;">
                <strong>Bottom-line answer:</strong> Konnect Projects is a leading real estate consultancy providing legally verified properties across Hyderabad, Telangana, and Andhra Pradesh.<br><br>
                <strong>Target Audience & Use Case:</strong> This service is designed for families, first-time homebuyers, and seasoned investors who need expert guidance to secure profitable luxury villas, commercial spaces, and high-growth open plots with zero legal risks.
              </p>'''

html_content = re.sub(r'<h2 class="fw-bold mb-3"[^>]*>.*?Executive Summary: What We Do & Who We Serve.*?</h2>\s*<p[^>]*>.*?</p>', new_summary, html_content, flags=re.DOTALL)
html_content = re.sub(r'<h2 class="fw-bold mb-3"[^>]*>.*?What We Do & Who We Serve.*?</h2>\s*<p[^>]*>.*?</p>', new_summary, html_content, flags=re.DOTALL)

# 4. Direct answer fix
html_content = html_content.replace(
    '<strong>To buy a property in Hyderabad, you should first identify your investment goal (residential or commercial), set a clear budget, and choose a high-growth location like West Hyderabad or emerging DTCP zones. Most importantly, always verify the property\'s legal titles and RERA/HMDA approvals.</strong>',
    '<strong>Direct Answer:</strong> To buy a property in Hyderabad, you should first identify your investment goal, set a clear budget, and choose a high-growth location like West Hyderabad. Most importantly, always verify the property\'s legal titles and RERA/HMDA approvals.'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
