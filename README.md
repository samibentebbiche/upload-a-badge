# upload-a-badge

This is the code for uploading a circular badge with a size of 512x512 pixels. It also verifies that the only non-transparent pixels are within the circular region, and the badge's colors evoke a 'happy' feeling. The process is simple; I classify images with more yellow pixels and higher intensity as happy pictures. There are two files involved.
## requirement 
- python3.
- PIL

## convert_badge.py
This code is to convert any image to a badge image.
To run the code just type in the commend line 
```
python convert_badge.py "the_path_of_the_image"
```
## verify_badge.py
This code is to verify if the image is circle and with the size of 512*512 and with a happy color feeling.
To run it just type in the commend line 
```
python verify_badge.py
```

