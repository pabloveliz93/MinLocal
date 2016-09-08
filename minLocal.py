def findlocalR(A,mid,N):
	if A[mid-1] > A[mid] and A[mid+1] > A[mid]:
		return A[mid]
	elif A[mid-1] > A[mid] and A[mid+1] < A[mid]:
		return findlocalR(A,N-(mid/2,N)
	else:
		return findlocalR(A,mid/2,mid)

def findlocal(A):
	return findlocalR(A,len(A)/2,len(A))

if __name__ == '__main__':

	
