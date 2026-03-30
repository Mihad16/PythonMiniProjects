
print('----------'
    'CALCULATOR'
    '----------')

def additional(num1,num2):
    additional=num1+num2
    return additional

def subtraction(num1,num2):
    subtraction=num1-num2
    return subtraction

def  multipication(num1,num2):
    multipication=num1*num2
    return multipication

def division(num1,num2):
    division=num1/num2
    return division

def modules(num1,num2):
    modules=num1%num2
    return modules
def squared(num1):
    squared=num1**2
    return squared

while True :
    print("1: additional")
    print("2: subtraction")
    print("3: multipication")
    print("4: division")
    print("5: modules")
    print("6: squared")
    print("7: exit")
    options = input("Select your option (1/2/3/4/5/6) :")

    if options == '7':
        print("exited")
        break
    if options =='6':
        num1=int(input("Enter a Number :"))

        print("__________________")
        print("Result :", squared(num1))
    if options in ('1','2','3','4','5',):
        num1 = int(input("Enter a First Number :"))
        num2 = int(input("Enter a Second Number :"))

        if options == '1':
            print("__________________")
            print("Result :", additional(num1, num2))
            print("==================")
        elif options == '2':
            print("__________________")
            print("Result :", subtraction(num1, num2))
            print("==================")
        elif options == '3':
            print("__________________")
            print("Result :", multipication(num1, num2))
            print("==================")
        elif options == '4':
            print("__________________")
            print("Result :", division(num1, num2))
            print("==================")
        elif options == '5':
            print("__________________")
            print("Result :", modules(num1, num2))
            print("==================")
        else:
            print("Invalid Options")






