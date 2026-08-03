import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace all <div class="d-flex flex-column gap-3"> inside the appreciation section with ul
# Replace all <div class="p-4 rounded-3" with <li class="p-4 rounded-3" if inside those uls.

# The easiest way is to use regex only on the Market Appreciation Section.
match = re.search(r'<!-- Market Appreciation Section -->.*?</section>', content, re.DOTALL)
if match:
    section_content = match.group(0)
    # Replace div with ul
    section_content = section_content.replace(
        '<div class="d-flex flex-column gap-3">',
        '<ul class="d-flex flex-column gap-3 list-unstyled m-0 p-0">'
    )
    # Replace ending </div> for those specific divs with </ul>.
    # Wait, simple replace is risky if I don't balance tags.
    # Let's just do it explicitly for the ones we added!
    
    section_content = section_content.replace(
        '<div class="p-4 rounded-3"',
        '<li class="p-4 rounded-3"'
    )
    section_content = section_content.replace(
        'Price Growth</div>\n              </div>',
        'Price Growth</div>\n              </li>'
    )
    # The container ul closing tags
    section_content = section_content.replace(
        '</li>\n            </div>',
        '</li>\n            </ul>'
    )
    
    # Also for the single item Residential Apartments
    section_content = section_content.replace(
        'Residential Apartments</h3>\n            <li class="p-4 rounded-3"',
        'Residential Apartments</h3>\n            <ul class="list-unstyled m-0 p-0"><li class="p-4 rounded-3"'
    )
    section_content = section_content.replace(
        '300% Price Growth</div>\n            </li>',
        '300% Price Growth</div>\n            </li></ul>'
    )

    content = content[:match.start()] + section_content + content[match.end():]

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
