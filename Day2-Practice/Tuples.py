from calendar import c
from re import T


tuple=(1,2,"HI")
print(tuple)
print(tuple[2])

#slicing
print(tuple[0:2])

tuple2= "a","b","c"
print(tuple+tuple2)

tuple3=(5,4,6,8,7,2,4)
#sorting 
print(sorted(tuple3))

#nested tuples
print(tuple[2][0])

#immutable
#tuple3[3]="hi"
new_tuple3=tuple3[0:3]+ ("Numbers",) + tuple3[4:]
print(new_tuple3)

#packing unpacking
t=(1,2,3,4)
(a,b,c,d)=t
print(b)