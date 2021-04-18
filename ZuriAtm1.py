import datetime
print(datetime.datetime.now())
name= input("Enter your name? \n")
allowedUsers= ['Himms', 'Nana', 'Ameed']
allowedPassword = ['passHimms', 'passNana', 'passAmeed']
if (name in allowedUsers):
    password=input("Your Password? \n ")
    userID = allowedUsers.index(name)
    if(password == allowedPassword[userID]):
        print("Welcome %s" %name)
        print("These are the available options")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaints")
        selectedOption = int(input("Please select an option: "))
        if(selectedOption == 1):
          #  print("You selected option %s " %selectedOption)
            withdraw = int(input(" How much would you like to withdraw: "))
            print("Take your Cash")
        elif(selectedOption == 2):
           # print("You selected option %s " %selectedOption)
            deposit = int(input(" How much would you like to deposit: "))
            print(deposit)
        elif(selectedOption == 3):
            #print("You selected option %s " %selectedOption)
            complaints = input(" What issue will you like to report? ")
            print("Thank you for contacting us")
        else:
            print("Invalid option selected, please try again")
    else:
        print("Password is incorrect please try again")
    
else:
    print("Name not found please try again")
