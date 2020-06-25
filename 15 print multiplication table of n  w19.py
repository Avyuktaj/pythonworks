##PRINT A MULTIPLICATION TABLE
##INT()FUNCTION : The int() function converts the specified value into an integer number.
##INPUT
##The input() function reads a line entered on a console by an input device such as a keyboard and convert it into a string and returns it.
##FOR LOOP
##A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)
print("__________________________________________________________________________________________________________________________________")
print("__________________________________________________________________________________________________________________________________")

