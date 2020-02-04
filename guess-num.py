import random

r = random.randint(1, 100)
i = 0
while True:
	num = int(input('請輸入猜的數字：'))
	i += 1
	print('已猜',i,'次')

	if num == r:
		print('恭喜你猜對了！！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')