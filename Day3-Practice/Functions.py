#lambda
input_list = ['9','6']
a = int(input_list[0])
b = int(input_list[1])

#Write your code here
greater=lambda x,y:x if x>y else y

print(greater(a,b))