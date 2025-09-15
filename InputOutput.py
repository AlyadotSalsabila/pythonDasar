print ("Input")
name = str (input ("What is your name : "))
age = int (input ("What's your age : "))
print ("Name: ", name)
print ("Age: ", age)

print ("Output")
# normal print
print ("Hi all! I am", name, "age", age, "years old")

# format print
print (f'Hi all! I am {name} age {age} years old')

# format print
print (f'Hi all! I am %s age %d years old' % (name, age))
# format output
print (30*"=")
print ("Temperature Calculator Program")
print (30*"=")