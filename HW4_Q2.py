import math

num1=input("Enter number")
num2=input("Enter number")
def checkValueIsNumber(inputStr: str):
   if inputStr != None and not inputStr.isspace() and inputStr.count(".") <= 1:
       inputStr = inputStr.replace(".", "1")
       if inputStr.isdigit():
          return True
   return False
check_num1=checkValueIsNumber(num1)
check_num2=checkValueIsNumber(num2)


if  check_num1 and check_num2 :
    num1 = float(num1)
    num2 = float(num2)




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
