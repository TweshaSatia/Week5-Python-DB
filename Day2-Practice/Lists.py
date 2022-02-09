#Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969). Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element, and convert it back to a tuple.

input_tuple = ('Monty Python', 'British', 1969)
list=list(input_tuple)
list.append("Python")
tuple_2=tuple(list)
print(tuple_2)

