import numpy as np
import random
#lsd = [1,2,3,4,5]
#als = np.array(lsd)
#
#print(als[1], als[4], lsd[1], lsd[4])
#print(als *2, lsd*2)
#
#list_a = [1, 2, 3]
#list_b = [4, 5, 6]
#
#array_a = np.array([1, 2, 3])
#array_b = np.array([4, 5, 6])
#
#print(list_a + list_b)
#print(array_a + array_b)
#
#l = list(als)
#print("l", l)
#
#nums = [1, 2, 3, 4, 5]
#nums_array = np.array(nums)
#
#print(sum(nums))
#print(np.sum(nums_array))
#
#list_2d = [[1, 2], [3, 4]]
#array_2d = np.array([[1, 2], [3, 4]])
#
#print(list_2d[1][1])
#print(array_2d[1, 1])
b= 10
arr = np.array([random.randint(1,10)for _ in range(b)])
q=""
for i in range(b // 2) :
q= q+str(arr[i])
print(q)
arr[3] = np.max(arr)
print(arr)
arr01 = np.array([random.randint(0,1)for _ in range(b)])
arrm = (arr+5) *3
print(arrm)
arms= sum(arr)
print(arms)
arre = arr*2
print(arre)