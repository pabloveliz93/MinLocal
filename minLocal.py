from random import randint

def fuerzabruta(arreglo) :
    N = len(arreglo)
    for i in range(1,N-1) :
        if arreglo[i-1] > arreglo[i] and arreglo[i+1] > arreglo[i] :
            return i

def randomwalk(tamano):
    W = [ randint(-1, 1) for _ in range(tamano)]
    A = list(accumulate(W))
    return A

def arr_knuth(arreglo, tamano) :
    for i in range(0,tamano) :
        arreglo.append(i)
    for i in range(1,tamano) :
        j = randint(0, tamano - 1)
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

def arr_rand_knuth(arreglo, tamano) :
    for i in range(0,tamano) :
        j = randint(0, tamano - 1)
        arreglo.append(j)
    for i in range(1,tamano) :
        j = randint(0, tamano - 1)
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

def arr_aleatorio(arreglo, tamano) :
    for i in range(0,tamano) :
        j = randint(0,tamano)
        arreglo.append(j)

def arr_ascendente(arreglo, tamano) :
    for i in range(0, tamano):
        arreglo.append(i)

def arr_descendiente(arreglo, tamano) :
    for i in range(0, tamano):
        arreglo.append(tamano - i)

def arr_swap_des(arreglo, tamano, k = 1) :
    for i in range(1, tamano):
        arreglo.append(tamano - i)
    arreglo.insert(k,0)

def arr_swap_as(arreglo, tamano, k = None) :
    if k is None :
        k = tamano - 2
    for i in range(0, tamano - 1):
        arreglo.append(i)
    arreglo.insert(k,0)

def arr_binario(arreglo, tamano) :
    for i in range(0, tamano):
        j = randint(0, 1)
        arreglo.append(j)

def arr_bin_unico(arreglo, tamano) :
    arreglo.append(0)
    for i in range(1,tamano) :
        arreglo.append(1)
    j = randint(0, tamano - 1)
    arreglo[0], arreglo[j] = arreglo[j], arreglo[0]

def arr_ceros(arreglo, tamano) :
    for i in range(0, tamano):
        arreglo.append(0)

def arr_sierra(arreglo,tamano) :
    N = tamano
    crec = True
    j = tamano//2
    while True :
        M = randint(1,(tamano//10))
        for i in range(0,M) :
            arreglo.append(j)
            N -= 1
            if N == 0 :
                return
            if crec :
                j += 1
            else :
                j -= 1
        if crec :
            crec = False
        else :
            crec = True

def arr_cordillera(arreglo,tamano) :
    N = tamano
    crec = True
    j = tamano//2
    while True :
        M = randint(1,(tamano//10))
        pend = M//5
        if pend == 0 :
            pend = 1
        for i in range(0,M) :
            k = randint(0,pend)
            arreglo.append(j)
            N -= 1
            if N == 0 :
                return
            if crec :
                j += k
            else :
                j -= k
        if crec :
            crec = False
        else :
            crec = True


def findlocalR(A,mid,low,hi):
	if mid>=hi or low>=hi:
		return -1
	if A[mid-1] >= A[mid] and A[mid+1] >= A[mid]:
		print (mid)
		return mid
	elif A[mid-1] > A[mid] and A[mid+1] < A[mid]:  # \
		return findlocalR(A,int(mid/2),mid,hi)
	else:
		return findlocalR(A,int(mid/2),0,mid)

def findlocal(A):
	return findlocalR(A,int(len(A)/2),0,len(A))

if __name__ == '__main__':
	from timeit import Timer
	from  sys import stdin
	A=[]
	arr_aleatorio(A,8000000)
	samples=4
	t=Timer("findlocal(A)", "from __main__ import findlocal, A")
	took = t.timeit(samples)/samples
	print("findlocal for {} integers took {:.7f} secs".format(len(A),took))