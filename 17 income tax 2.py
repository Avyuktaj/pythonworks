age = int(input("Enter Age : "))
salary = int(input("Enter salary : "))
if age>=55:
    print("your tax is",salary*10/100)
else:
   if salary >= 1500000 and 2000000 :
       print("your tax is",salary*15/100)
   else:
       if salary >= 2000000 and 2500000 :
           print("your tax is",salary*20/100)
       else:
           if salary >= 2500000 and 3000000 :
               print("your tax is",salary*25/100)
           else:
               if salary >= 3000000 and 100000000 :
                   print("your tax is",salary*30/100)
         

         










