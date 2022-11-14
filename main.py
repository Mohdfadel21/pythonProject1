# x = type(5.5) is int  #للمقارنة
# print(x)
# # contain for search if this text contain a value
# text = "Hello world"
# i = "HEllo" in text
# print(i)
#
# # in قبلها قيمة البحث و بعدها مكان البحث
#
#
#
#
#
#
# is_student = False
#
#
# if (5<10) and not (5>2):
#   if 55==5:
#      print("YEs he is Student")
# elif 55==25 :
#  print("No he is not")
#
#
#
#
carname = "Volvo "


input_number= input("Enter number")
mm="mm"
if input_number.isdigit() and input_number.isspace() and not input_number.find(" "):

    cast_num = int(input_number)
    if cast_num % 2 == 0:
         print("even")

    else:
        print("odd")

else:
 print("Invalid Value")



# input the list
A = list(map(int, input('Enter elements of List: ').split()))

# create two empty lists to store EVEN and ODD elements
B = []
c = []

MOG="ga"

for j in A:
    if j % 2 == 0:
        B.append(j)
    else:
        c.append(j)

print('List of even number: ', B)
print('List of odd number: ', c)
