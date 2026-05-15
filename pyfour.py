names=[]
while True:
    print("shop menu\n 1:display all items\n 2:add items at the end\n 3:add items at specific index\n 4:delete item by name\n 5:delete item at specific position\n 6:exit")
    choice=int(input("enter your choice: "))
    #display all items
    if choice==0:
        print(f"thank you, welcome back, your new list is :{names}")
        break

    #display all items
    elif choice==1:
        print(names)

    # add items at the end
    elif choice==2:
        item=input("enter add the items: ")
        names.append(item)
        print(names)

    #add items at specific index
    elif choice==3:
        item=input("enter the item name")
        index=int(input("enter your index position"))
        names.insert(index,item)
        print(names)

    #delete enter by name
    elif choice==4:
        item=input("enter your choice")
        names.remove(input("write the name to delete"))
        print(names)

        #delet items at a specific position
    elif choice==5:
        names.pop(int(input("enter your index")))
        print(names)

    else:
        print("invalid input")
            


         








      
    








