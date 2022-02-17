while True :
    x = int(input("enter first number : "))
    y = int(input("enter second number : "))
    a = int
    z = input("select operation \n + \n - \n * \n / \n")
    if z ==  "+":
            a = x+ y
            print(x, "+", y,"=",a)
            # break
    elif z== "-":
            a = x-y
            print (a)
            # break
    elif z == "*":
            a = x*y
            print(a)
            # break

    elif z=="/":
            a = x/y
            print(a)
            # break
        
    print("Do you want to try again : ")
    again= input("Yes = Y or No = N \n")
    if again == "N":
        print("Thank you!")
        break
