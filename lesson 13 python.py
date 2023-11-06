import pandas as pd

baby_names = pd.read_csv("US_Baby_Names_right.csv")

#See the first 10 entries

baby_names.head(10)

#Delete the column 'Unnamed: O' and 'Id'

baby_names = baby_names.drop(["Unnamed: 0", "Id"], axis= 1)

#Is there more male or female names in the dataset ?

baby_names.Gender.value_counts()

#Group the dataset by name and assign to names

bb = baby_names.groupby("Name").sum()
print(bb)

#How many different names exist in the dataset ?

noms_comptes = len(baby_names['Name'].value_counts())
print(noms_comptes)

#What is the name with most occurences ?

names_occ = baby_names['Name'].value_counts()
print(names_occ)
max = names_occ.max()
print(max)


#Euro 2012 data set
euro12 = pd.read_csv("Euro_2012_stats_TEAM.csv")

euro12.columns

euro12['Goals']

len(euro12.Team.unique())

euro12.shape

#New table with values we need

discipline= euro12[['Team','Yellow Cards', 'Red Cards']]

#Ascending is by croissant order (=1), decroissant order(=0)

discipline.sort_values(by='Red Cards', ascending=0)

#Head() alone is the 5 first columns

discipline.sort_values(by='Yellow Cards', ascending = 0).head()

discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

discipline['Yellow Cards'].mean()

def calc_goals(x):
  if x >=6:
    return x
