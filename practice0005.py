'''
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。1136*640

'''

from PIL import Image
import glob
def get_pic(path):
    all_pic=glob.glob(path+'/*.jpg')
    return all_pic


def pic_process(name,number):
    im = Image.open(name, 'r')

    w, h = im.size
    if w > 1136:
        h = 1136 * h / w
        w = 1136
    if h > 640:
        w = 640 * w / h
        h = 640
    im.thumbnail((w,h))
    im.save(str(number)+'.jpg','jpeg')
def main():
    path='E:/PyCharm 5.0.3/untitled3'
    all_pic=get_pic(path)
    number=1
    for each in all_pic:
        pic_process(each,number)
        number+=1


if __name__=='__main__':
    main()



