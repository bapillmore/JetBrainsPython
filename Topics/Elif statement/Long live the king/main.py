column = int(input())
row = int(input())

if column in [1,8] and row in [1,8]:
	print(3)
elif column in [1,8] and row in [2,3,4,5,6,7]:
	print(5)
elif column in [2,3,4,5,6,7] and row in [1,8]:
	print(5)
else:
	print(8)