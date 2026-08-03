import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <form id="contactForm" ...> with POST and csrf
old_form = '''<form id="contactForm" class="p-4 rounded-4" style="background: var(--light-bg); border: 1px solid var(--border);">'''
new_form = '''<form id="contactForm" method="POST" action="{% url 'core:submit_enquiry' %}" class="p-4 rounded-4" style="background: var(--light-bg); border: 1px solid var(--border);">
              {% csrf_token %}'''
html = html.replace(old_form, new_form)

# Add name attributes
html = html.replace('id="formName" required', 'id="formName" name="name" required')
html = html.replace('id="formPhone" required', 'id="formPhone" name="phone" required')
html = html.replace('id="formEmail" class="form-input"', 'id="formEmail" name="email" class="form-input"')
html = html.replace('id="formLocation" class="form-input', 'id="formLocation" name="location" required class="form-input')
html = html.replace('id="formBudget" class="form-input', 'id="formBudget" name="budget" required class="form-input')
html = html.replace('id="formMessage" rows="3"', 'id="formMessage" name="message" rows="3"')
html = html.replace('name="propType" value=', 'name="propType" required value=')
html = html.replace('name="timeline" value=', 'name="timeline" required value=')

# Also remove javascript intercepting the form
html = re.sub(r'document\.getElementById\([\'"]contactForm[\'"]\)\.addEventListener\([\'"]submit[\'"].*?\}\);', '', html, flags=re.DOTALL)
html = re.sub(r'document\.getElementById\(\'contactForm\'\)\.addEventListener\(\'submit\'.*?\}\);', '', html, flags=re.DOTALL)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated index.html form')
