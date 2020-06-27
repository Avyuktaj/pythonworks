##22 June: calcluate the tax payable for salary input the annual salary and age conditions: if age <55 tax is 10%
##( irrepspective of salary range) tax range: up to 15 L 10% 15 to 30 L >> 15% 30 to 40 L >> 20% 40L to 99L >>30% more than 99L >>35%
age = int(input("Enter Age : "))
salary = int(input("Enter salary : "))
tax=5
if age<=55:
   print("tax",tax) 
if tax==10:
   print("15L to 20L")
if tax==15:
   print("20L to 30L")
if tax==20:
   print("30L to 40L")
if tax==25:
   print("40L to 50L")
if tax==25:
   print("50L to 99L")    
