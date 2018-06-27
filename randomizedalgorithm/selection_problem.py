
import random


def partition(arr, p, r):
	x = arr[r]
	i = p - 1
	for j in range(p, r):
		if arr[j] <= x:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[r] = arr[r], arr[i+1]
	return i+1


def randomized_partition(arr, p, r):
	i = random.randint(p, r)
	arr[r], arr[i] = arr[i], arr[r]
	return partition(arr, p, r)


def randomized_select(arr, p, r, i):
	if p == r:
		return arr[p]
	q = randomized_partition(arr, p, r)
	k = q - p + 1
	if i == k:
		return arr[q]
	elif i < k:
		return randomized_select(arr, p, q-1, i)
	else:
		return randomized_select(arr, q+1, r, i-k)


if __name__ == '__main__':
	arr = [2,8,7,1,3,5,6,4]
	p = 0
	r = 7
	print(arr)
	res = randomized_select(arr, p, r, 5)
	print(arr)
	print(res)
