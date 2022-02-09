#Write code to fetch the profession of the employee with Employee id - 104 from an employee input given in the form of a dictionary where key represent employ id and values represent the name, age, and profession (in the same order).
input_dict = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}
Employee_list = list( input_dict[104])
profession = Employee_list[2]
print(profession)

#Create a SORTED list of all values from the dictionary input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}
input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}
ans=sorted(input_dict.values())
print(ans)