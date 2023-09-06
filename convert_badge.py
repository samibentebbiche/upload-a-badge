from PIL import Image, ImageDraw, ImageOps
import sys

#read the image 
input_image_path = sys.argv[1]
output_badge_path = "output_badge.png"

def convert_to_badge(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)

        if img.size != (512, 512):
            #return False, "Image size must be 512x512."
            img.resize((512,512),Image.BICUBIC).save("resized.png")
            img = Image.open("resized.png")



        mask = Image.new('L', (512, 512), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 512, 512), fill=255)
        
        output = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        output.paste(img, mask=mask)

        output.save(output_path)
        
        return True, "Image converted to badge successfully."

    except Exception as e:
        return False, str(e)


is_converted, conversion_message = convert_to_badge(input_image_path, output_badge_path)

print(conversion_message)