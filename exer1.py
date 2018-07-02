person_you_know = []
answer = ""
person_name = ""

def who_do_you_know():

    loop_me = True
    while loop_me == True:
        answer = input("Enter the name of person, enter 'X' to stop: ")
        if(answer != 'X'):
            person_name = answer
            person_you_know.append(person_name)
        else:
            loop_me = False
            print("You know these people {}!".format(person_you_know))
        
def ask_user():
    answer = input("Enter a name of person: ")

    for name in person_you_know:
        if(answer == person_you_know[])

who_do_you_know()