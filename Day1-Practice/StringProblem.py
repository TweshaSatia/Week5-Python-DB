#Description
#In a certain encrypted message which has information about the location(area, city), the characters are jumbled such that first character of the first word is followed by the first character of the second word, then it is followed by second character of the first word and so on
#In other words, let’s say the location is bandra,mumbai
#The encrypted message says ‘bmaunmdbraai’.

input_str = input("Enter encrypted message")
message1=input_str[0::2].rstrip('#')
message2=input_str[1::2].rstrip('#')
print(message1 + "," + message2)