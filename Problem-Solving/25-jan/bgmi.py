C_match = int(input("Enter number of Matches Played :"))#current match played
Finish = int(input("Enter number of Finish in This Season :"))#current Finish
Finish_required = 3*(100 + C_match) - Finish#finish needed
if Finish_required <= 0:
    print("KD of 3 cannot be achived ")
else:
    print("Required kills are : " + str(Finish_required))
