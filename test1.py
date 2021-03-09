#A couple of functional programming primitives like the filter() function, the map() function, and the reduce() function and how those correspond to some other things that are actually built into Python, like list comprehensions.
import collections
from pprint import pprint
Scientist = collections.namedtuple('Scientist',['name', 'field', 'born' , 'nobel'])
#print(Scientist)
ob1 = Scientist(name = "Ava" , field = "math" , born = 1815 , nobel = False)
ob2 = Scientist(name = "Berry" , field = "physics" , born = 1900 , nobel = False)
tuple_Scientists = (ob1,ob2)
#pprint(tuple_Scientists)

#filter

fs = filter(lambda x : x.nobel is False, tuple_Scientists)

#pprint(fs)

#pprint(next(fs))
#pprint(next(fs))

#tuple

print("*****")
fs = tuple(filter(lambda x : x.field=="math", tuple_Scientists))
#pprint(fs)


#list comprehension

ls = [x for x in tuple_Scientists if x.nobel is False ]

#pprint(tuple(ls))

#pprint(tuple(x for x in tuple_Scientists if x.nobel is False ))

#map function python

#pprint(tuple_Scientists)

names_and_ages = tuple(map(lambda x:{'name':x.name , 'age':2021-x.born} , tuple_Scientists))


#pprint(names_and_ages)

#reduce

from functools import reduce

print(tuple_Scientists)
print(names_and_ages)

total_age = reduce(
        lambda acc,val: acc+val["age"] , names_and_ages , 0
)

print(total_age)

#pythonic way

total_age= sum(x["age"] for x in names_and_ages)
print(total_age)


print(tuple_Scientists)

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientist_field = reduce(reducer,tuple_Scientists , {"math" : [] , "physics":[]})

pprint(scientist_field)


import collections

scientist_field = reduce(reducer,tuple_Scientists , collections.defaultdict(list))

pprint(scientist_field)


























