# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import random


def add_num(img):
	draw = ImageDraw.Draw(img)
	fonts = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', size=40)
	w, h = img.size
	rndNum = str(random.randint(0, 99))
	rndColor = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	draw.text((w-50, 0), rndNum, font=fonts, fill=rndColor)
	img.save('result.jpg', 'jpeg')

if __name__ == '__main__':
	img = Image.open('image.jpg')
	add_num(img)