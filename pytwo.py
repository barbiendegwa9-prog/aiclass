names=[]
while True:
    print("Students Menu\n1. Add user\n2.Add user at a specific index\n 3.Delete a user\n 4.delete a user at a certain postion\n 0.exit\n ")
    choice=int(input("enter your choice: "))
    #add user
    if choice==0:
        print(f"thank you, Welcome back, your new list is : {names}")
        break

    #add user
    elif choice==1:
        student=input("enter you name: ")
        names.append(student)
        print(names)
    #add user at specific index
    elif choice==2:
        student=input("enter your name ")
        index=int(input("enter your index "))
        names.insert(index, student)
        print(names)

 #delete user by name
    elif choice==3:
        names.remove(input("write the name to delete: "))
        print(names)

    #delete user at specific position
    elif choice==4:
        names.pop(int(input("enter your index: ")))
        print(names)

    #display users
    elif choice==5:
        print(names)

    #delete at a specific index
    elif choice==6:
        del names[int(input("enter your index: "))]
        print(names)

    else:
        print("invalid input")











        
        
    



        




    


    




        







