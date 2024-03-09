from PIL import Image
import pilgram

im = Image.open('paisagem.jpg')
pilgram.xpro2(im).save('paisagem-xpro2.jpg')