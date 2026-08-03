import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# I will replace <div class="d-flex flex-column gap-3"> with <ul class="d-flex flex-column gap-3 list-unstyled m-0 p-0"> 
# and the inner <div class="p-4 rounded-3" with <li class="p-4 rounded-3"
# But I must be careful to only do this inside the Market Appreciation section.
# A simpler way is to just add a list somewhere in the document. The SEO report just says "Lists: 0".
# Let's add a small checklist in the new Key Takeaway section instead, because it's easier and safer!
# Wait, I already added a checklist in the Key Takeaway! Let's just change those divs to a ul/li.

content = content.replace(
    '<div class="d-flex flex-wrap gap-4">',
    '<ul class="d-flex flex-wrap gap-4 list-unstyled m-0 p-0">'
).replace(
    '<div class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">For Homebuyers & Investors</span>\n                </div>',
    '<li class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">For Homebuyers & Investors</span>\n                </li>'
).replace(
    '<div class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">100% Legally Verified Properties</span>\n                </div>',
    '<li class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">100% Legally Verified Properties</span>\n                </li>'
).replace(
    '<div class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">High ROI Locations</span>\n                </div>\n              </div>',
    '<li class="d-flex align-items-center gap-2">\n                  <i class="fas fa-check-circle fs-5" style="color: var(--gold);"></i>\n                  <span class="fw-medium text-dark" style="font-size: 0.95rem;">High ROI Locations</span>\n                </li>\n              </ul>'
)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
