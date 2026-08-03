
with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/rekonnect_project/settings.py', 'a', encoding='utf-8') as f:
    f.write('\n# Whitenoise Compression & Caching\n')
    f.write('STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"\n')
print('Appended')
