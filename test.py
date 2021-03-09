#func prog -> mainly use immutable data structures and we try to avoid side effects by doing all of our computation using the evaluation of mathematical functions.

#rule 1: immutable data structure


import collections
from pprint import pprint
Scientist = collections.namedtuple('Scientist',['name', 'field', 'born' , 'nobel'])

#print(Scientist)

ob1 = Scientist(name = "Ava" , field = "math" , born = 1815 , nobel = False)
ob2 = Scientist(name = "Berry" , field = "physics" , born = 1900 , nobel = False)

Scientists =[ob1,ob2]

pprint(Scientists)

del Scientists[0]

pprint(Scientists)


# instead of list use tuple since its immutable

tuple_Scientists = (ob1,ob2)
pprint(tuple_Scientists)












