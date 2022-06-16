import image2ascii
from PIL import Image

print("")
print("----------------------------------------------------------------")
print("image2ascii v1.0 by hw2007")
print("If the art doesn't come out properly, lower your font size")
print("----------------------------------------------------------------")
print("")

img_path = input("Image to convert to ASCII art (path): ")
img = Image.open(img_path)
res = int(input("Width (176 is recommended): "))
img = img.resize([res, int(res/img.width*img.height)])
img = img.convert("L")
img_load = img.load()

for row in image2ascii.convert(img, img_load):
    print(row)
