import numpy as np
import matplotlib as plt


def ex1():
    v = np.array(21)
    v[9:16] *= -1
    print(v)


def ex2():
    v = np.array(15, 56)
    r = v[1:-1]
    print(r)


def ex3():
    a = np.array(12).reshape(3, 4)
    for row in a:
        for value in row:
            print(value, end=' ')


def ex4():
    x = np.linspace(10, 50, 10)
    print(x)


def ex5():
    vector = np.empty(5, dtype=int)
    for i in range(5):
        while True:
            try:
                value = int(input(f"Enter an integer between 0 and 10 for element {i + 1}: "))
                if 0 <= value <= 10:
                    vector[i] = value
                    break
                else:
                    print("Value must be between 0 and 10. Try again.")
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 10.")
    print("User-defined vector:", vector)


def ex6() :
    v1 = np.array([2,4,5,5,6])
    v2 = np.array([2,5,3,1,9])
    v3 = np.matmul(v1,v2)

    print(v3)

def ex7() :
    mat = np.zeros((3,4))

    for i in range (0,3) :
        for j in range (0,4) :
            mat[i,j] = np.random.randint(10,22)
    print(mat)


def ex8() :
    matrxxx = np.ones((5,6))
    a,b = matrxxx.shape
    print("rows : " +str(a) +"\ncolumns : "+str(b))

def ex9() :
    mat = np.zeros((4,4))
    mat[1::2,1::2] = 1
    mat[::2,::2] = 1
    print(mat)

def ex10() :
    Array1= np.array([0,10,20,40,60,10,10,30],dtype=int)
    Array2= np.array([10,30,40,70,45,23,40],dtype=int)
    Array3 = []
    print(Array1)
    print(Array2)


    for i in range (0,len(Array1)) :
        for j in range (0,len(Array2)) :
            if (Array1[i] == Array2[j]) :
                Array3.append(Array1[i])

    A3 = np.unique(Array3)
    print(A3)

def ex11() :
    Array1 = np.array([0, 10, 20, 40, 60, 10, 10, 30], dtype=int)
    print(Array1)
    A2 = np.unique(Array1)
    print(A2)

def ex12() :
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print(v1)
    print(v2)

    cross_product = np.cross(v1, v2)


    print(cross_product)

def ex13():
    mat = np.zeros((10,2))
    for i in range (0,10) :
        for j in range (0,2) :
            mat[i,j] = np.random.randint(-10,10)

    x = mat[:, 0]
    y = mat[:, 1]
    r = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)
    deg = np.degrees(theta)
    polmat = np.column_stack((r, deg))
    print(mat)
    print(polmat)

def ex14() :
    n = float(input("choose a value between 0 and 99 : "))
    a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,
50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,
75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
)
    sp = 99999999999
    b=0
    k=0
    for i in range (0,len(a)) :
        b=abs(a[i]-n)
        if (b<sp) :
            sp=b
            k=i
    print("the closest value of "+format(n)+" is "+format(a[k]) + " at the index "+ format(k))








