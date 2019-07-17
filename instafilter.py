# Import Image from PIL
from PIL import Image
#load images into objects 
base_img= Image.open("potrait.jpg")

# set o/p image size
size=(760,760)
#resize all images to o/p size
base_img= base_img.resize(size) #for resizing

#split each image into rgb
r,g,b = base_img.split()

#to merge all the pictures
im=Image.merge("RGB", (r, g, B))
im.show()
#im.save(1_merge.jpg)