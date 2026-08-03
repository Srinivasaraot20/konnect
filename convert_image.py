from PIL import Image
import os

png_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/image.png'
webp_path = 'c:/Users/ASUS/Downloads/rekonnect1/rekonnect/static/image.webp'

if os.path.exists(png_path):
    try:
        with Image.open(png_path) as img:
            # Resize image to something smaller like 400px width
            wpercent = (400 / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((400, hsize), Image.Resampling.LANCZOS)
            img.save(webp_path, 'webp', quality=85)
            print("Successfully converted and resized image to webp!")
    except Exception as e:
        print(f"Error converting image: {e}")
else:
    print("image.png not found!")
