students=[]
staffs=[]
while True:
    print(" student menu\n 0:exit\n 1:add staffs\n 2:add students\n 3:delete staffs\n 4:delete students\n 5:view staffs\n 6:view students")
    choice=int(input("enter your choice: "))
    if choice==0:
        print(f"thank you, welcome back, your new list is :{staffs} and {students}")
        break

    #add staffs
    elif choice==1:
        staffs.append(input("enter your staff name: "))
        print("staffs", staffs)

    #add students
    elif choice==2:
        students.append(input("enter your student name: "))
        print("students", students)

    #delete staffs
    elif choice==3:
        staffs.remove(input("write the staffs to delete: "))
        print("staffs", staffs)

    #delete students
    elif choice==4:
        students.pop(int(input("enter your student index: ")))
        print("students", students)

    #view staffs
    elif choice==5:
        print("staffs", staffs)

    #view students
    elif choice==6:
        print("students", students)

    else:
        print("invalid input")





