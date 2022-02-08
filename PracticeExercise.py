#Consider the string given below and answer the following questions 
from pickletools import string4


string = "OQYWFClFhFGAvIWYwGKpmZhnJiyzTslSIhSwvOsqJMEphzmifTkyqOMNpnOtXZxmCfgDYqbaBHAUvIWhMnvwZnEMVDvmEfLrDoQnAZgQEgXQVnmSYkfedpAdhrtpOgORpYLRZYGWdhWYuqQssCUXtTzKRDAhpjUheOzUroZNzWFtZOVwIapzUYtbSbjYNErzQ"

#no. of characters
print("No. of characters",len(string))

#no. of occurences of a
print("No. of occurences of a",string.count("a"))

print("Starts with if or not? ",string.startswith("if"))

#63 to 88
print(string[63:89])

print(string[45])
