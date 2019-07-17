from PIL import Image

base_img= Image.open("potrait.jpg")
img_filter= Image.open("download.jpeg") #opening image

size=(760,760)

base_img= base_img.resize(size) #for resizing
img_filter=img_filter.resize(size)

r,g,b = base_img.split()
R,G,B= img_filter.split()

im=Image.merge("RGB", (r, g, B))
im.show()
#im.save(1_merge.jpg)