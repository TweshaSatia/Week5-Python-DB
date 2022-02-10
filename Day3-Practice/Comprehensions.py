#List Comprehension
#You are given an integer 'n' as the input. Create a list comprehension containing the squares of the integers from 1 till n^2 (including 1 and n), and print the list. 

n = int(input())
def squares(n):
    L = [i*i for i in range(1,n+1)]
    return L

print (squares(n))

