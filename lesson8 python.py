#dictionnary

country_capitals={
"United states" : "Washington D.C",
"Italy":"Rome",
"England":"London"
}
print(country_capitals)

country_capitals={
"United states" : "Washington D.C",
"Italy":"Rome",
"England":"London"
}
print(country_capitals["Italy"]) #afficher un élément du dico

#supprimer un element du dico
country_capitals={
"United states" : "Washington D.C",
"Italy":"Rome",
"England":"London"
}

del country_capitals["United states"]
print (country_capitals)

#pour tout mettre a 0 mettre le nom du dico.clear()
----------------------------------------------------------------
my_dict={
1: "Hello",
(1,2): "Hello Hi", # on ne peut pas appeler la definition par une liste ( le truc avant les 2 points)
3:[1,2,3]    
}

print(my_dict)
----------------------------------------------------
#creating dictionnary
Dict=dict({1:'Geeks',2:'For',3:'Geeks'})
print("\nDictionnary with the use of dict():")
print(Dict)

#ou sinon 
Dict1=dict([(1,'Geeks'),(2,'For')])
print("\nDictionnary with the use of dict():")
print(Dict1)

#dico dans un dico
Dict={1:'Geeks',2:'for',
      3:{'A':"Welcome",'B':"Bye"}}
--------------------------------------------------

Dict={"Dict1":{1:'Geeks'},
      'Dict2':{"Name":'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1]) #ecrire l'élément du 1er dico dans le dico principal
print(Dict['Dict2']['Name'])#ecrire l'élément du 2e dico

#pour changer une valeur on ecrit juste le nom du dico crochet la def à changer = a la nouvelle valeur
#ex pour Italie:Naples pour changer cette erreur on met dico['Italie']='Rome'
#de meme pour ajouter une valeur
-------------------------------------------------------
.pop() ->remove the item with the specific key
.update() -> add or change dico items
.clear()
.keys() ->returns all the dico keys
.values() ->returns all the dico values
.get() ->returns the value of the specific keys
.popitem() ->returns the last inserted key and value as a tuple
.copy() -> returns a copy of the dico
-------------------------------------------------------------
#ecrire deux list dans un dico
keys=('Ten','Twenty','Thirty')
values=(10,20,30)
res_dict=dict(zip(keys,values)) #permet d'écrir qu'un seul tuple au lie des tous les 3 , la fonction formkey
print(res_dict)
-------------------------------------------------------------
#exrire deux dico et update le dico 1 avec le reste du dico2
dict1={'Ten':10, 'Twenty': 20, 'Thirty':30}
dict2={'Thirty':30, 'Forty': 40, 'Fifty':50}
dict1.update(dict2)
print(dict1)

----------------------------------------------------------------
employees=['Kelly','Emma']
default={"designation":'Developer',"Salary":8000}
res=dict.fromkeys(employees,default)
print(res)
------------------------------------------------------------
remove things from a dictionary
sample_dict={
    "name":"Kelly",
    "age":25,
    "Salary":8000,
    "city":"New York"
    }

sample_dict.pop("name")
sample_dict.pop("Salary")
print(sample_dict)

