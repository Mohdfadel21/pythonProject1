num1=input("Enter num1")
num2=input("Enter num2")
num3=input("Enter num3")
num4=input("Enter num4")
num5=input("Enter num5")

arr_num=[num1,num2,num3,num4,num5]
print(arr_num)




#################################################3
if arr_num[0] > arr_num[1] and arr_num[0] > arr_num[2] and arr_num[0] > arr_num[3] and arr_num[0] > arr_num[4]:
    print("the large number is :", arr_num[0])

elif arr_num[1] > arr_num[0] and arr_num[1] > arr_num[2] and arr_num[1] > arr_num[3] and arr_num[1] > arr_num[4]:
    print("the large number is :", arr_num[1])

if arr_num[2] > arr_num[1] and arr_num[2] > arr_num[0] and arr_num[2] > arr_num[3] and arr_num[2] > arr_num[4]:
    print("the large number is :", arr_num[2])

elif arr_num[3] > arr_num[0] and arr_num[3] > arr_num[2] and arr_num[3] > arr_num[1] and arr_num[3] > arr_num[4]:
    print("the large number is :", arr_num[3])

elif arr_num[4] > arr_num[0] and arr_num[4] > arr_num[1] and arr_num[4] > arr_num[2] and arr_num[4] > arr_num[3]:
    print("the large number is :", arr_num[4])


 ###########################################################################################


if arr_num[0] < arr_num[1] and arr_num[0] < arr_num[2] and arr_num[0] < arr_num[3] and arr_num[0] < arr_num[4]:
    print("the smallest number is :", arr_num[0])

elif arr_num[1] < arr_num[0] and arr_num[1] < arr_num[2] and arr_num[1] < arr_num[3] and arr_num[1] < arr_num[4]:
    print("the smallest number is :", arr_num[1])

if arr_num[2] < arr_num[1] and arr_num[2] < arr_num[0] and arr_num[2] < arr_num[3] and arr_num[2] < arr_num[4]:
    print("the smallest number is :", arr_num[2])

elif arr_num[3] < arr_num[0] and arr_num[3] < arr_num[2] and arr_num[3] < arr_num[1] and arr_num[3] < arr_num[4]:
    print("the smallest number is :", arr_num[3])

elif arr_num[4] < arr_num[0] and arr_num[4] < arr_num[1] and arr_num[4] < arr_num[2] and arr_num[4] < arr_num[3]:
    print("the smallest number is :", arr_num[4])
