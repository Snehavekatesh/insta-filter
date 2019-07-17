# Import Image from PIL
from PIL import Image
#load images into objects 
base_img= Image.open("potrait.jpg")
img_filter= Image.open("download.jpeg") #opening image
# set o/p image size
size=(760,760)
#resize all images to o/p size
base_img= base_img.resize(size) #for resizing
img_filter=img_filter.resize(size)
#split each image into rgb
r,g,b = base_img.split()
R,G,B= img_filter.split()

im=Image.merge("RGB", (r, g, B))
im.show()
#im.save(1_merge.jpg)