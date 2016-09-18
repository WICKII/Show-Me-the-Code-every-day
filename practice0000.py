from PIL import Image,ImageDraw,ImageFont
import random
im=Image.open('headpic.jpg','r')
msgnum=str(random.randint(1,99))

w,h=im.size
wDraw=w*0.8
hDraw=w*0.08
#draw the num
font=ImageFont.truetype('c://Windows/Fonts/Arial.ttf',30)
draw=ImageDraw.Draw(im)
draw.text((wDraw,hDraw),msgnum,font=font,fill=(255,33,33))


im.save('headpicadd.png','png')

immodify=Image.open('headpicadd.png')
immodify.show()

