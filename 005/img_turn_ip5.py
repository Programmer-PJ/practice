# coding:utf-8
# 把图片的尺寸变成都不大于 iPhone5 分辨率的大小


from PIL import Image


def change_size(file, size=(1136, 640)):
	size = (size[1], size[0]) if file.size[1] > file.size[0] else size
	file.thumbnail(size, Image.ANTIALIAS)
	file.save('resule.jpg', 'jpeg')

if __name__ == '__main__':
	file = 'test.jpg'
	im = Image.open(file)
	change_size(im)
