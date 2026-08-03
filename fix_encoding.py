html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('Hyderabad â€“ 500081', 'Hyderabad &ndash; 500081')
html_content = html_content.replace('â€“', '&ndash;')
html_content = html_content.replace('â‚¹', '&#8377;') # Replace broken rupee symbols too just in case

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
