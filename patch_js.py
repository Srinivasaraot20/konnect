import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'document\.getElementById\([\'"]contactForm[\'"]\)\.addEventListener\([\'"]submit[\'"].*?\}\);', '', js, flags=re.DOTALL)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('Updated main.js')
