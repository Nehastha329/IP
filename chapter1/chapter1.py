
from PIL import Image
import numpy 
print('neha')
image = Image.open('a.jpg').convert('LA')
image.save('greyscale.png')
image.show()


image1=Image.open('a.jpg')
image1.show()

images = Image.open("greyscale.png")
new = numpy.array(images)
print (new)






