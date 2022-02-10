#Using the function Map, count the number of words that start with ‘S’ in input_list.
input_list =['Santa Cruz','Santa fe','Mumbai','Delhi']
count = list(map(lambda x:x[0]=='S',input_list)).count(True)
print(count)

#Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively. 
input_list1 = [ ['Ankur','Avik','Kiran','Nitin'],['Narang','Sarkar','R','Sareen']]
first_name = input_list1[0]
last_name = input_list1[1]

name = list(map(lambda f,l:f + " " + l, first_name, last_name))
print(name)

#Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
input_list2=['soap','sharp','shy','silent','ship','summer','sheep']
sp = list(filter(lambda x: x[0]=='s' and x[-1]=='p' , input_list2))#Write your code here

print(sp)

from functools import reduce

#Find and print the largest number in input_list using the reduce() function.
input_list3=[65,76,87,23,12,90,99]
print(reduce(lambda x, y: x if x > y else y,input_list3))
