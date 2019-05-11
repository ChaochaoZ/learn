print('******************************')
print('********   (*^__^*)    *******')
print('*******欢迎使用超超计算器********')
print('*******超超未来会是大牛哦********')
print('*******  颤抖吧凡人们！ ********')
print('******************************')

count = 1

while True:
	print('请开始你的第' + str(count) + '次运算')
	a = float(input('请输入第一个数字: '))
	b = float(input('请输入第二个数字: '))
	act = int(input('''请输入计算方式\n加法输入1\n减法输入2\n乘法输入3\n除法输入4: '''))

	ret = 0

	if act == 1:
		ret = a + b
	elif act == 2:
		ret = a - b
	elif act == 3:
		ret = a * b
	elif act == 4:
		ret = a / b
	else:
		ret = '非法操作'

	print('>>>结果是：' + str(ret))
	print('***********')
	count += 1
