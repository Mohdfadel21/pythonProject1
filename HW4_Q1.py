

name=input("Enter name")
address=input("Enter address")
age=input("Enter age")



if name.isdigit() or name.isspace():
 print("invalid input")
 quit()




if  address.isdigit() or address.isspace():
 print("invalid input")


print()




check_age=age.isspace()

if age.isdigit() :
 if isinstance(age, float):
  age=int(age)
 print("Hello Mr/Ms : ", name , "age : ", age , "located in :" , address , "thanks for being in our community ,\t Enjoy")




else:
 quit()






