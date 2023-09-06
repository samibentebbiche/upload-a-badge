# upload-a-badge

This is the code to upload a circle badge with a size of 512*512.
And verify that the only non-transparent pixels are within a circle and the colors of the badge give a "happy" feeling.
I worked simple , i give the images with more yellow pixel and with hight intensity as a happy pictures.
ther is two file .
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

