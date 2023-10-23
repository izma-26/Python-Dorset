COURS 2:

#comment écrire une formule

R= 0.0820
n=0.5
T=298.15
V=5.0
p=n*R*T/V
print ("At temperature {} K the pressure is {} atm.".format(T,p))


#exemple de comment faire pour écrire des phrases avec des valeurs
a=2
b=3
area=a*b
print("The area of the edge rectangle {} and {} is valide {}.".format(a,b,area))

i=5
i=i+1
print(i)


a=5 # réel
c=3 #imaginaire
b=complex(a,c)
print(b)

a=3
b=float(a)
print("The variable b is {}".format(b))
b=3.8
c=int(b)
print("The variable c is valide {}".format(c))

#// division euclidienne
#% modulo

a=5
b=3
c=2.5
cal=(2*a+b**2)/c
print(cal)


myname=input("Enter your name")  
print(myname) # l'ordinateur pose une question


R=0.08206
n=input("Enter the number of moles:")
n=float(n)
T=input("Enter the temperature in K:")
T=float(T)
V=input("Enter volume in L:")
V=float(V)
p=n*R*T/V
print("Gas pressure is {} atm".format(p))

#ou sinon

R=0.08206
n=float(input("Enter the number of moles:"))
T=float(input("Enter the temperature in K:"))
V=float(input("Enter volume in L:"))
p=n*R*T/V
print("Gas pressure is {} atm".format(p))


#exercic1 Find the volume
r=10
h=3
pi=3.14
V=(1/3)*pi*h*r**2
print(V)

r=10
h=5
pi=3.14
V=(1/3)*pi*h*r**2
print(V)

r=15
h=2
pi=3.14
V=(1/3)*pi*h*r**2
print(V)

r=12
h=5
pi=3.14
V=(1/3)*pi*h*r**2
print(V)

import math #pour mettre des valeurs de maths 
r=12
h=5
V=(1/3)*math.pi*h*r**2
print(V)


import math
dir(math) #donne toutes les opérations que math fait

import math as m
ang=float(input("Enter an angle in sexagesimal degrees: "))
ang_rad=ang*m.pi/180#convert the angle in radians
si=m.sin(ang_rad)#the sine is calculated
print("The sine of {} is {}".format(ang,si))

#ex2

num1=float(input("Enter a numeric value:"))
num2=float(input("Enter another numeric value:"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1,num2,sum))
print("The product of {} and {} is {}".format(num1,num2,product))

import math as m
ang=float(input("Enter an angle in sexagesimal degrees: "))
ang_rad=ang*m.pi/180#convert the angle in radians
si=m.sin(ang_rad)#the sine is calculated
print("The sine of {} is {}".format(ang,si))

#ex2

num1=float(input("Enter a numeric value:"))
num2=float(input("Enter another numeric value:"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1,num2,sum))
print("The product of {} and {} is {}".format(num1,num2,product))

#ex convertir degree en Kelvin
T=float(input("Enter the temperature in Celsius: "))
Kel=T+273.15
print("The temperature {}Celsius is {}K".format(T,Kel))

#exercice volume et aire d'un carre
c=float(input("Enter the length of the edge of a cube:"))
area=6*c*c
volume=c*c*c
print("The area of the cube whom lenght is {} is {} cm^2".format(c,area))
print("The volume of the cube whom lenght is {} is {} cm^3".format(c,volume))

#exercice ou on demande le nombre de billets qu'une personne a et la somme que cela fait 
n10=int(input("Enter the number of 10 euro you have"))
n20=int(input("Enter the number of 20 euro you have"))
n50=int(input("Enter the number of 50 euro you have"))
sum=n10*10+n20*20+n50*50
print("If the user has {} tickets of 10 euros, {} of 20 euros and {} of 50 , in total he has {} euros".format(n10,n20,n50,sum))

#exercice ou on demande la longueuer et l'air d'un cercle
import math
rad=float(input("Enter the radius of the circle"))
L=2*math.pi*rad
A=math.pi*rad**2     #math.exp()
print("For a radius of {} cm the length of the circuference is {}cm and the value of the area is {} cm^2".format(rad,L,A))

# meme chose mais pour une sphere
import math
rad=float(input("Enter the radius of the sphere"))
V=4/3*math.pi*rad**3
A=4*math.pi*rad**2
print("For a radius of {} cm the length of the circuference is {}cm and the value of the area is {} cm^2".format(rad,V,A))


#exercice avec une formule de constante de réaction
import math
A=float(input("Enter the A value:"))
Ea=float(input("Enter the Ea value:"))
T=float(input("Enter the temperature in Kelvin:"))
T=T+273.15
R=8.314
k=A*math.exp(-Ea/(R*T))
print("the rate constant is {}".format(k))

#exercice sur la longueur des cotes d'un triangle
import math
a=float(input("Enter the first side of the traingle"))
b=float(input("Enter the second side of the triangle"))
ang=float(input("Enter the angle in degree"))
c=math.sqrt(a**2+b**2-(2*a*b*math.cos(math.radians(ang))))
print("Given a triangle of side {} and {}, and a angle of {}° between them , the third side is {}".format(a,b,ang,c))

print(223/71)
print((1+1/10)**10)
print((1+1/100)**100)
print((1+1/1000)**1000)
