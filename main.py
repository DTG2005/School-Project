import Dependencies.Classes as Classes
import Dependencies.Behaviour as B
import Dependencies.Weapons_and_Armour as WA

while True:
    response = input("Do you want to create a new profile or quit? (N/Q)")
    if response == "Q":
        break
    else:
        response = int(input("Creating a new profile, choose class to proceed:-\n\n1. Mage: High damage but low defence\n2. Knight: Balanced damage and defence\n3. Castellan: High defence but low damage."))
        
        if response == 1:
            print("You are now a Mage!!")
        elif response == 2:
            print("You are now a Knight!!")
        elif response == 3:
            print("You are now a Castellan!!")

        name = input("Enter your name during this adventure.")
        print("Your name has now been registered as {}!!! Let us begin your journey...".format(name))

        en1 = Classes.spawn(Classes.Enemy(), WA.Small_Club)
    
        B.EnterCombatMode()