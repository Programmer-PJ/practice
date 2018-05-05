# coding:utf-8
# 任一个英文的纯文本文件，统计其中的单词出现的个数


import re
import pandas


def catch(file):
	with open(file, 'r') as f:
		s = f.read()
		words = re.findall(r'[a-zA-Z0-9]+', s)
		return ''.join(words)

def count(words):
	c = {}
	for i in words:
		i = i.lower()
		if i in c:
			c[i] += 1
		else:
			c[i] = 1
	return c


if __name__ == '__main__':
	w = catch('test.txt')
	c = count(w)
	s = pandas.Series(c)
	print(s)