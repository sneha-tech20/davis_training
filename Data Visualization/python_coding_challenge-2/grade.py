marks = int(input(" Enter the marks of student:"))
if(marks>=90):
    print("grade A")
elif(marks<=89 or marks>=70):
    print("grade B")
elif(marks<70  or marks >=50):
    print("grade C")
    
else:
    print("fail")            