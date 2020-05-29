import math

r = input('输入圆的半径:')

def area(r):
	try:
		area = int(r) ** 2 **math.pi
	#输入数值错误时抛出异常
	except ValueError:
		print('请输入整数数值为半径')
		exit()

	#raise语句的作用:主动抛出异常的关键字
	if int(r) > 11:
		raise ImportError('半径数值太大')
	print('圆的面积等于{:.2f}'.format(area))

if __name__ == '__main__':
	#对area函数的异常值进行处理
	try:
		area(r)
	#如果数值大于11会抛出这个异常,e的值为异常提示信息
	except ImportError as e:
		print(e)
		exit()
