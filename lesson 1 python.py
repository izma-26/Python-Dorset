COURS 1:

>>> print("Goodbye,cruel world!")
Goodbye,cruel world!

>>> type('Name') #permet de donner le type
<class 'str'>
>>> name = '431'                             ┌───────────────────────────┐
>>> name2 = '56'
>>> add = name + name2
>>> print(add)
43156
>>> name = 431
>>> name2 = 21
>>> add= name + name2
>>> print(add)
452
>>> print(""" hello python,
... how areyou doing""")
hello python,
how areyou doing
>>> print("hello python\how are you doing")
hello python\how are you doing
>>>
    print("hello python\nhow are you doing")
hello python
how are you doing

exercice ou on fait toutes les opérations sur 2 nbs
>>> num1=5
>>> num2=25
>>> add=num1+num2
>>> print(add)
30
>>> div=num2/num1
>>> print(div)
5.0
>>> mult=num1*num2
>>> print(mult)
125
>>> exp=num1**num2
>>> print(exp)
298023223876953125

exercice ou il faut additionner 2 float et les changer en string
>>> num1= 3,14
>>> type(num1)
<class 'tuple'>
>>> num2=3.14
>>> num3=1.7128
>>> print(num2+num3)
4.8528
>>> num4=str(num2)
>>> num5=str(num3)
>>> print(num4+num5)
3.141.7128


>>> print("coffee\n café\n caffé\n Kaffee)
  File "<stdin>", line 1
    print("coffee\n café\n caffé\n Kaffee)
          ^
SyntaxError: unterminated string literal (detected at line 1) -> erreur la ou ya un signe

>>> print('coffee\ncafé\ncaffé\nKaffee')
coffee
café
caffé
Kaffee

exercice ou on doit demander a l'utilisateur un nombre , il nous répond un float et il faut ajouter 2.5
>>> print("How much?") # exemple de ce qui ne marche pas 
How much?
>>> a=input(2.7)
2.7+2.5
>>> print("a"+2.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str


>>> pay= float(input("How much?"))
How much?2.9
>>> print(pay+2.5)
5.4

>>> 'sparrow'>'eagle'
True
>>> 'dog'>'cat' or 45%3==0
True
>>> 60-45/5+10==1
False


signe 
maths                    python
=  (name=value)           == (compare, num1==num2)
différent                 !=






