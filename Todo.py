odo_list = []
def addlist():
    item = input("enter a Item")
    todo_list.append(item)
    print(f"{item} added to Todo lis")

def displaylist():
    print("------------------")
    if not todo_list:
        print("nothinh")
    else:
     print("Print Tod List")

    for index, item in enumerate(todo_list,start=1):
         print(f"{index} - {item}")
def remove():
    displaylist()
    index= int(input("enter your itenm ti rEMOVE"))-1

    if  0<= index < len(todo_list):
        removed_item=todo_list.pop(index)
        print(f"{removed_item} remoevd fromn tyhe list")
    else:
        print("invalid")

while True:
    print("++++++++++++++++++++++++")
    print("ToDo list App")
    print("++++++++++++++++++++++++")
    print(" 1 - Add To List")
    print(" 2 - Display List")
    print(" 3 - RemoveList")
    print(" 4 - Exit")
    option = input("Select your Options :")
    if option == '1':
        addlist()
    elif option == '2':
        displaylist()
    elif option == '3':
         remove()
    elif option == '4':
        break
    else:
        print("Invalid option")