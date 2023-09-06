from PIL import Image, ImageDraw, ImageOps

input_image_path = "output_badge.png"

def verify_badge(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Verify image size is 512x512
        if img.size != (512, 512):
            return False, "Image size must be 512x512."
        
        # Verify that only non-transparent pixels are within a circle
        mask = Image.new('L', (512, 512), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 512, 512), fill=255)
        
        non_transparent = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        non_transparent.paste(img, mask=mask)
        
        if non_transparent.tobytes() != img.tobytes():
            print(non_transparent.tobytes())
            print(img.tobytes())
            return False, "Non-transparent pixels must be within a circle."
        
        # Verify the colors of the badge
        # if the color of the median is more yelow then the image have happy color
        average_color = img.convert("RGB").resize((1, 1)).getpixel((0, 0))
        print(average_color)
        # You can define your criteria for happy colors here.
        happy_color_criteria = lambda color: color[0] > 100 and color[1] > 100 and color[2] < 100
        if not happy_color_criteria(average_color):
            return False, "Colors do not give a 'happy' feeling."
        
        # If all verifications pass, the image is valid
        return True, "Badge image is valid."

    except Exception as e:
        return False, str(e)


is_valid, message = verify_badge(input_image_path)
print(message)