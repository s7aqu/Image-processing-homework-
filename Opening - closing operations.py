from PIL import Image, ImageFilter
import psutil
import time

# open and show image
img = Image.open('mini.png')
img.show()

# blur the image
filtered_image_blur = img.filter(ImageFilter.BLUR)
filtered_image_blur.save('mini_blur.png', 'png')
filtered_image_blur.show()

# change color of image to black and white
filtered_image_grey = img.convert('L')
filtered_image_grey.save('mini_grey.png', 'png')
filtered_image_grey.show()

# change orientation of image
funny_image = filtered_image_grey.rotate(180)
funny_image.save('mini_grey_rotated.png', 'png')
funny_image.show()

filtered_image_grey_jpeg = img.convert('L')
filtered_image_grey_jpeg.save('mini_grey.jpeg', 'jpeg')

time.sleep(10)

# close the preview of the all images opened in a new window
for proc in psutil.process_iter(): # traverse the current process
    if proc.name() == "Preview": # process is Preview
        proc.kill()
