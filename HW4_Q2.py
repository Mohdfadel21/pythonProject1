import math

num1=input("Enter number")
num2=input("Enter number")

check= (num1.isspace() or num1.isdigit()) and (num2.isdigit() or num2.isspace() )
if check == "false" :
    print("invalid")

else :
    num1=int(num1)
    num2=int(num2)



input_operaretor=input("Select one operaretor : 1_ + \n 2_ - \n3_ *\n4_ /\n5_ ^ \n6_ % \t ")

sum=0

if input_operaretor=="1" or input_operaretor=="+" :
   sum= num1+num2
   print("The sum is : ", sum)
elif input_operaretor=="2" or input_operaretor=="-" :
    sum = num1 - num2
    print("The sum is : ", sum)
elif input_operaretor=="3" or input_operaretor=="*" :
    sum = num1 * num2
    print("The sum is : ", sum)
elif input_operaretor=="4" or input_operaretor=="/" :
    sum = num1 / num2
    print("The sum is : ", sum)
elif input_operaretor=="5" or input_operaretor=="^" :
    sum = num1 ^ num2
    print("The sum is : ", sum)
elif input_operaretor=="6" or input_operaretor=="%" :
    sum = num1 % num2
    print("The sum is : ", sum)



more_option= input("1_ Normal rounding, up or down a number \n 2_ Take the number without a decimal point \n 3_ Exit")


if more_option=="1" or input_operaretor=="Normal rounding, up or down a number" :
 print(math.floor(sum))
elif more_option=="2" or input_operaretor=="Take the number without a decimal point" :
    print(math.ceil(sum))
elif more_option=="3" or input_operaretor=="Exit" :
     quit()



print("thanks")
