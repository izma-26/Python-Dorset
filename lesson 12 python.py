import matplotlib.pyplot as plt
import numpy as np

def ex1() :

    #%matplotlib inline

    x=np.linspace(-2,2,101)
    y=x**2

    plt.plot(x,y)
    plt.show()

def ex2() :

    #%matplotlib inline
    x=np.linspace(0,3*np.pi,500)

    plt.plot(x,np.sin(x**2))
    plt.title("a simple chirp")
    plt.show()

def ex3() :

    #matplotlib inline
    x=np.linspace(-2,2,101)
    y=x**2
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(-1.5,1.5)
    plt.ylim(-0.5,2.5)
    plt.title("Chart Title")
    plt.plot(x,y)
    plt.show()

def ex4() :

    #matplotlib inline

    x=np.linspace(-2,2,101)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    y=x**2
    plt.plot(x,y,label = "x^2")
    y2=x**4
    plt.plot(x,y2,label="x^4")
    plt.legend()
    plt.show()
def ex5() :

    #matplotlib inline

    n = int(input("number of points to draw : "))
    x = np.linspace(-1,1,n)
    y=np.cos(2*np.pi*x)
    plt.plot(x,y,"o")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("cos function with "+str(n)+" points")
    plt.savefig("cos2pix.png")
    plt.show()


def ex6() :
    #matplotlib inline
    n = int(input("number of points to draw : "))
    x = np.linspace(-1,1,n)
    y=np.cos(2*np.pi*x)
    y2= np.sin(2 * np.pi * x)
    plt.plot(x,y,"x",label="cos(2pix)")
    plt.plot(x, y2, "x",label="sin(2pix)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("cos function with "+str(n)+" points")
    plt.legend()
    plt.savefig("trigo.png")
    plt.show()

def ex7() :
    #matplotlib inline

    n = int(input("number of points to draw : "))
    x = np.linspace(0,4,n)
    y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
    plt.plot(x,y,"+")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("special function with "+str(n)+" points")

    plt.savefig("experience.png")
    plt.show()

def ex8() :
    #matplotlib inline

    n = int(input("number of points to draw : "))
    x = np.linspace(2,10,n)
    y=(0.08206*300)/x
    plt.plot(x,y,"+")
    plt.xlabel("Vm")
    plt.ylabel("P")
    plt.title("P in function of Vm with "+str(n)+" points")

    plt.savefig("isotherme.png")
    plt.show()

def ex9() :
    x0 = int(input("x0 : "))
    s = float(input("s : "))
    # matplotlib inline

    n = int(input("number of points to draw : "))
    x = np.linspace(x0-2, x0+2, n)
    y = (1/(np.sqrt(2*np.pi)))*np.exp((-1/2)*((x-x0)**2)/(s**2))
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gaussian function of Vm with " + str(n) + " points")

    plt.savefig("gaussian.png")
    plt.show()

def exo10() :
    #matplotlib inline
    n = int(input("number of points to draw : "))
    x = np.linspace(0,3,n)
    y=np.exp(-x)
    y2= np.sin(3 * np.pi * x)*np.exp(-x)
    plt.plot(x,y,label="e^-x")
    plt.plot(x, y2,label="sin(3pix)*e^-x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("e^-x and sin(3pix)*e^-x function with "+str(n)+" points")
    plt.legend()
    plt.savefig("trigo.png")
    plt.show()

def exo11() :
    # matplotlib inline
    n = int(input("number of points to draw : "))
    num = int(input("enter number of function to draw : "))
    for i in range (0,num) :
        x0 = int(input("x0 : "))
        s = float(input("s : "))



        x = np.linspace(x0 - 2, x0 + 2, n)
        y = (1 / (np.sqrt(2 * np.pi))) * np.exp((-1 / 2) * ((x - x0) ** 2) / (s ** 2))
        plt.plot(x, y)
        plt.plot(x, y, label="Gaussian,x0="+str(x0)+",s="+str(s))
        plt.legend()

    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.title("Gaussian functions with " + str(n) + " points")

    plt.savefig("gaussian_complex.png")
    plt.show()







