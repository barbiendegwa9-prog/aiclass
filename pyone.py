name=["john", "barbie","kristie", "sam","kelvin","mitchell"]
print(name)
print(name[0])
name.append("gabriel")
print(name)
name.insert(3, "sandra")
print(name)
newstudent=["mary", "melissa", "maggie", "grace", "preshi", "caroline"]
name.extend(newstudent)
print(name)
name.remove(input("Write the name to delete: "))
print(name)
name.pop(4)
print(name)
del name[5]
print(name)