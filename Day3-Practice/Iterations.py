#You are given a list of string elements and asked to return a list which contains each element of the string in title case or in other words first character of the string would be in upper case and remaining all characters in lower case
input_list=['VARMA', 'raj', 'Gupta', 'SaNdeeP']
updated_list= []

for i in input_list:
    updated_list.append(i.capitalize())
    
print(updated_list)