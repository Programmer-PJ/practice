# coding:utf-8
# 验证码生成器


import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


size = (240, 60)

def gen_random():
    charlist = [random.choice(string.ascii_uppercase) for i in range(4)]
    chars = ''.join(charlist)
    return chars

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def gen_captcha():
    im = Image.new('RGB', size, color = 0)
    draw = ImageDraw.Draw(im)
    for w in range(size[0]):
        for h in range(size[1]):
            draw.point((w, h), random_color())
    chars = gen_random()
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', int(size[1]*0.8))
    x = 0
    y = size[1] * 0.1
    for i in range(4):
        x += size[0] * 0.2
        draw.text((x, y), chars[i], font=fnt, fill=random_color())
    im = im.filter(ImageFilter.BLUR)
    im.save('captchar.jpg')


if __name__ == '__main__':
    gen_captcha()
