users = ['Alex','Audree']
passwrd = ['123','456']
check = False


inp = input("Enter User : ")
if inp in users:
    while check == False:
        inp_pas = input("Enter Password : ")
        if inp == 'Alex' and inp_pas == '123':
            print("Yes")
            check = True
        elif inp == 'Audree' and inp_pas == '456':
            print('Yes')
            check = True
        else:
            print("Password incorrect try agin")
else:
    print("No user Try again!")