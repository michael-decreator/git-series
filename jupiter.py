
print ("\nTHIS IS A SIMPLE CALCULATOR\n")

print ("1.multiplication\n2.addition\n3.subtraction\n4.division\n")
num1 = int 
num2 = int 
ans = int
response = int
response = int (input ("please select the operation you want to use: "))



if response == 1:
   num1 = int(input ("enter first number: "))
   num2 = int(input ("enter second number: "))
   ans = (num1*num2)
   print  (f"{num1} x {num2} = {ans}" )
   

elif response == 2:  
   num1 = int(input ("enter first number: "))
   num2 = int(input ("enter second number: "))
   ans = (num1 + num2)
   print  (f"{num1} + {num2} = {ans}" )


elif response == 3:  
   num1 = int(input ("enter first number: "))
   num2 = int(input ("enter second number: "))
   ans = (num1-num2)
   print  (f"{num1} - {num2} = {ans}" )



elif response == 4:  
   num1 = int(input ("enter first number: "))
   num2 = int(input ("enter second number: "))
   ans = (num1/num2)
   print  (f"{num1} / {num2} = {ans}" )


else: 
   print ("invalid input")
   print ("thank you fool")  
   
 






    








