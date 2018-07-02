my_variable = "Vrylle"


loop_me = True
while loop_me == True:
    print(my_variable)

    user_input = input("Should we print the name again? y/n: ")
    if(user_input == 'n'):
        loop_me = False
        print("Thank you for your reply!")