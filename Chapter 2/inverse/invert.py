from PIL import Image, ImageOps
import ImageOps
img=Image.open('1.png').convert('L')
imgs=ImageOps.invert(img)
img.show()
imgs.show()
imgs.save('2.png')
