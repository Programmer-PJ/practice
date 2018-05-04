# coding:utf-8
# 使用 Python 如何生成 200 个激活码（或者优惠券)

import random, string


def rand_str(num, length=7):
	with open('Activation_code.txt', 'w') as f:
		for i in range(num):
			chars = string.ascii_letters + string.digits
			s = [random.choice(chars) for i in range(length)]
			f.writelines(''.join(s) + '\n')


if __name__ == '__main__':
	rand_str(200)