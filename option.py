def option():
    user_option = input("WOULD YOU LIKE TO CONTINUE? y/n ")
    if user_option.upper() == "Y":
        pass
    elif user_option.upper() == "N":
        print("quitting....")
        quit()
    else:
        print("INVALID INPUT")    
