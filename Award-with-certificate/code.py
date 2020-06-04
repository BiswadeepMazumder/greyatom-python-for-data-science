# --------------
# Code starts here

# Create the lists 
class1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class=class1+class2
print(new_class)

# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)


# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)

# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`
Total=courses['Math']+courses['English']+courses['French']+courses['Science']+courses['History']

# Print the total
print (Total)
# Insert percentage formula
percentage= ((Total)/500)*100
# Print the percentage
print(round(percentage,2))



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
print(mathematics)

max_marks_scored = max(courses,key = courses.get)
print (max_marks_scored)

topper=max(mathematics,key=mathematics.get)
print(topper)
# Given string


# Create variable first_name 
first_name,last_name=topper.split()
print(last_name)
# Create variable Last_name and store last two element in the list

# Concatenate the string
full_name=last_name+" "+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here



