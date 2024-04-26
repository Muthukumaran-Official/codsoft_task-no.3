#this is my second project...password generator for my internship program at codsoft!!
#here we are going to ask the user about the size and complexity of the password that the user want and print/display the password accordingly!!


import random
while True:
    
    passchar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~@#$%^&*()_+|}{\|[];:'\,.<>?/"
    passcombo_no=int(input("enter the number of passwords you want to generate : "))
    passwrdlength=int(input("enter the length of the password : "))
    passcomplexity=int(input("\n 1.LOW\n 2.MEDIUM \n 3.HIGH \n 4.EXTREME \n enter the complexity number(1/2/3/4): "))

    if passcomplexity==1:
        print("you have choosen low complexity password")
    elif  passcomplexity==2:
        print("you have choosen medium complexity passowrd")
    elif  passcomplexity==3:
        print("you have choosen high complexity password")
    elif passcomplexity==4:
        print("you have choosen extreme complexity password")
    else:
        print("wrong option choosen....try again")
        continue
    for combinations in range(passcombo_no):
        validchar=[]
        if passcomplexity==1:
            for i in passchar:
                if i.isdigit():
                    validchar.append(i)
            password=random.choices(validchar,k=passwrdlength)
            print(''.join(password))
            

        elif passcomplexity==2:
            for i in passchar:
                if i.isalpha():
                    validchar.append(i)
            password=random.choices(validchar,k=passwrdlength)
            print(''.join(password))
            

        elif passcomplexity==3:
            for i in passchar:
                if i.isdigit() or i.isalpha():
                    validchar.append(i)
            password=random.choices(validchar,k=passwrdlength)
            print(''.join(password))
            

        elif passcomplexity==4:
            for i in passchar:    
                validchar.append(i)
            password=random.choices(validchar,k=passwrdlength)
            print(''.join(password))
    choice=int(input("do you want to continue???? \n 1.YES \n 2.NO \n enter the option number(1/2) : "))
    if choice==1:
        continue
    elif  choice==2:
        print("\n thanks for using......exiting program")
        break
    else:
        print("invalid option....its fine!!!...exiting program")
        break