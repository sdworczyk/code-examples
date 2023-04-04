participant = input("Please enter your name: ")
swimming = int(input("Please state the time of completion in minutes for the swimming event: "))
cycling = int(input("Please state the time of completion in minutes for the cycling event: "))
running = int(input("Please state the time of completion in minutes for the running event: "))
total = swimming + cycling + running
print("Congratulations on completing the triathlon", participant, "!", "Your total time is: ", total, " minutes.")
#Each discipline received its own input with float command. This helps with the addition of all times for the total string.
if (total <= 100): #More than or equal to sign makes sure that the right award is printed for the time provided.
    print("Well done! You receive a Provincial Colours award!")

elif (total > 100) and (total <= 105): #The range od more than and less than and equal signs makes sure to print appropriate message for time provided.
    print("Well done! You receive a Provincial Half Colours award!")

elif (total > 105) and (total <= 110): #The range od more than and less than and equal signs makes sure to print appropriate message for time provided.
    print("Well done! You receive a Provincial Scroll award!")

elif (total > 110): #A simple use of more than sign allows to print appropriate message.
    print("Well done! You have completed the triathlon. Unfortunately no reward is available for you at this time. Good luck next time!")