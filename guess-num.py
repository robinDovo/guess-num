import random
print('起始值為：1')
end = int(input('請輸入結束值：'))


r = random.randint(1, end)
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