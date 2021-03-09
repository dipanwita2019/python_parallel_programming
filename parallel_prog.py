import collections
from pprint import pprint
import concurrent.futures
import os

Scientist = collections.namedtuple('Scientist' , ['name',"field", "born","nobel"])

scientists = (Scientist(name = "ada" , field = "physics" , born =1970, nobel = True ),
              Scientist(name = "ben" , field = "maths" , born =1960, nobel = False ),
              Scientist(name = "polly" , field = "chem" , born =1930, nobel = True ),
              Scientist(name = "suzan" , field = "physics" , born =1980, nobel = False ),
              Scientist(name = "richard" , field = "chem" , born =1956, nobel = True ),
              Scientist(name = "mula" , field = "physics" , born =1970, nobel = False ),
              Scientist(name = "dereck" , field = "astronomy" , born =1920, nobel = True ),
              Scientist(name = "ben" , field = "physics" , born =1940, nobel = False )
                              )


pprint(scientists)
print()

import time
def transform(x):
    print(f"Process id :{os.getpid()} Processing started {x.name}")
    time.sleep(1)
    result = {'name': x.name , 'age' : 2021 - x.born}
    print(f"Process id :{os.getpid()} Done processing {x.name}")
    return result

start = time.time()

#result = tuple(map(transform , scientists))

#pool = multiprocessing.Pool()

with concurrent.futures.ProcessPoolExecutor() as executor:
    result = executor.map(transform, scientists)

end = time.time()

print(f"\nTime to completion {end -start:.2f}s\n")

pprint(tuple(result))
