full_name = input("Please enter your full name: ")

if(len(full_name) == 0):
    print("You did not enter anything. Please enter your full name.")
#The code makes sure that if nothing is entered, an appropriate error message prompts the user to correct it.
elif(len(full_name) <= 4):
    print("The name you have entered is too short. Please enter your full name.")

elif(len(full_name) > 4 and len(full_name) <= 10):
    print("Seems like you have only entered your name. Please enter your name and surname.")
#The two codes above make sure to alert the user if only their name has been entered and asks to enter name and surname.
elif(len(full_name) > 10 and len(full_name) <= 25):
    print("Thank you! Your name is " + full_name + ".")
#Upon successful provision of full name. A thank you message will appear with the user's name printed to double check.
elif(len(full_name) > 25):
    print("The name you have entered is too long. Please only enter first name and surname.")
#The code above makes sure to prompt the user to only enter their first name and surname if more than 25 characters were provided.