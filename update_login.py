html_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace(
    'href="{% url \'core:login\' %}"',
    'href="https://konnect-iota.vercel.app/" target="_blank" rel="noopener noreferrer"'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
