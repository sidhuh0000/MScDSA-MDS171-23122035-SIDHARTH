nameList=[] #global variable name list

def storeName():
    name=input("Enter the Name to be saved :")
    name = name.strip().title()
    nameList.append(name)
    return name 

def listNames():
    print("*"*30)
    print("Names in the List")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)


def searchName(search):
    search=search.strip().tittle()
    found = False
    for name in nameList:
        if name == search:
            found = True
            break
    if found == True:
        print("Name exist in the list")
    else:
        print("Name doesn't exit....!")



        


while True: 
    print("*"*30)
    print("1.Enter a Name")
    print("2.list the names")
    print("3.Search for a name")
    print("4.exit")
    print("*"*30)

    choice = input("Enter your choice ?")
    print("You have entered choice:", choice)

    if int(choice) == 1:
        name = storeName()
        print("Name{}added succesfully!",format(name))
    elif int(choice) == 2:
        listNames()
    elif int(choice)==3:
        name = input("Enter a name to be searched")
        searchName(name)
    elif int(choice)==4:
        exit()
    else:
        print("invaalid option...!")


