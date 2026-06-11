students=[]
staffs=[]
while True:
     print("student menu\n1.add staff\n2.add students\n3.delete staff\n4.delete student\n5.view staff\n6.view student\n7.exit")
     choice=int(input("enter your choice: "))
     #view staff
     if choice==0:
          print(f"thank you,welcome back,your new list is : {students},{staffs}" )
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
        
    

         



         



          


















                                                                                                                                       