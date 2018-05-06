# coding:utf-8
# 从英文文档中找出关键词


import re


def catch(file):
	with open(file, 'r') as f:
		s = f.read()
		w = re.findall(r'[a-zA-Z0-9]+', s)
		return w

def count(w):
	c = {}
	for i in w:
		if i in c:
			c[i] += 1
		else:
			c[i] = 1
	return c

def op(r):
	for i in range(5):
		print(r[i][0], end=' ')

if __name__ == '__main__':
	file = 'test.txt'
	words = catch(file)
	keywords = count(words)
	result = sorted(keywords.items(), key=lambda d:d[1], reverse=True)
	op(result)