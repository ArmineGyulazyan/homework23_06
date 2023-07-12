def merge(ls1, ls2):
	ls_merged = ls1 + ls2
	for i in range(len(ls_merged)):
		sorted = False
		for j in range(0,len(ls_merged)-i-1):	
			if ls_merged[j] > ls_merged[j+1]:
				temp = ls_merged[j]
				ls_merged[j] = ls_merged[j+1]
				ls_merged[j+1] = temp
				sorted = True
			
		if sorted == False:
			break
			
	return ls_merged

ls1 = [3,4,3]
ls2 = [1,2,8]


print(merge(ls1,ls2))