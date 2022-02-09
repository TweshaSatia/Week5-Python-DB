#removing duplicates
Grades = ['A', 'A', 'B', 'C', 'D', 'B', 'B', 'C', 'D', 'E', 'C', 'C', 'A', 'B', 'F', 'D', 'C']
print(set(Grades))

#Let’s say you have two lists A and B. Identify the elements which are common in the two lists A and B and return them in a sorted manner. For example 
#Sample Input :
#A = [5,1,3,4,4,5,6,7]
#B = [5,1,3,4,4,5,6,7]

list_1 = [5,1,3,4,4,5,6,7]
list_2 = [5,1,3,4,4,5,6,7]
set_1=set(list_1)
set_2=set(list_2)
answer1=set_1.intersection(set_2)
answer=list(answer1)
print(answer)

nums = set([1,1,2,3,3,3,4])
print(len(nums))