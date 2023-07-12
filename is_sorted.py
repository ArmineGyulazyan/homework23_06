def is_sorted(ls):
	count = 0
	for i in range(len(ls)-1):
		for j in range(i,len(ls)):
			if ls[i]>ls[j]:
				count += 1
			
	if count != 0:
		return False
	else:
		return True


ls_check = [3,5,7,8]
res = is_sorted(ls_check)
print(res)