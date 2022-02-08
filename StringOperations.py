#slicing of string
statement="Python is a programmming language"
sliced=statement[0:7]
print(sliced)
sliced1=statement[:8]
print(sliced1)
sliced2=statement[8:]
print(sliced2)

#membership
print('Python' in statement)
print('pro' not in statement)

#repeatition #len
x = 'len'
print(x[len(x*2)- 5])

#upper lower
print(statement.upper())
print(statement.lower())

#rstrip lstrip
string="%%%%%%44###"
print(string.rstrip('#').lstrip("%"))

#count
print(string.count("%"))

age=22
print(' I am {0} years old'.format(age))

