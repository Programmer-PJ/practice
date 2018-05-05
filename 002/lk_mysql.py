# coding:utf-8
# 激活码（或者优惠券）保存到 MySQL 关系型数据库中


import peewee, random, string

connect = peewee.MySQLDatabase(
	database = 'pj',
	host = '127.0.0.1',
	user = 'root',
	password = '123456',
	port = 3306,
	charset = 'utf8'
	)

class Coupon(peewee.Model):
	id = peewee.PrimaryKeyField()
	code = peewee.CharField(max_length = 32)
	class Meta:
		database = connect

class code_yield:
	def __init__(self):
		self.chars = string.ascii_letters + string.digits
	def rand_str(self, length=7):
		s = [random.choice(self.chars) for i in range(length)]
		return ( ''.join(s))

if __name__ == '__main__':
	try:
		Coupon.create_table()
	except Exception as e:
		print(e)
	num = input('增加n个优惠码：')
	for i in range(int(num)):
		c = Coupon()
		c.code = (code_yield().rand_str())
		c.save()


		