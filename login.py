my_dict = {'karenzi': '@12345'}



running = True
while running:
    user_response = input("ARE YOU NEW TO THE ALPHA KIDS APP?:  Y/N")
    if user_response.upper() == "Y":
        print("PLZ CREATE AN ACCOUNT")
        user_name = input("PLZ ENTER YOUR NAME: ")
        user_password = input("SET YOUR PASSWORD: ")
        my_dict[user_name] = user_password
        running = False
    elif user_response.upper() == "N":   
        run = True
        while run:
            print("PLZ LOGIN WITH VALID CREDENTIALS")
            username = input("PLZ ENTER YOUR NAME: ")
            userpassword = input("ENTER YOUR PASSWORD: ")
            if username in my_dict:
                if my_dict[username] == userpassword:                        
                    print("LOGIN SUCCESSFUL!")
                    run = False
                    running = False
                else:
                    print("INVALID CREDENTIALS..TRY AGAIN")
            else:
                print("INVALID USERNAME..TRY AGAIN")        
    else:
        print("INVALID INPUT")             

        
