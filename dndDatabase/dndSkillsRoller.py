import sqlite3
import random

#Connect method
conn = sqlite3.connect("dndDB.db")

#Executes SQL commands.
c = conn.cursor()


##################################
#  Get the information from Database.
##################################
def getInfo(choice):

    name = " "
    #Determine name of skill/attack.
    if choice == "a":
        name = input("What is the attack name?")
        c.execute("SELECT name FROM attacks WHERE name = ?", (name, ))

        #Add in the appropriate info if it's an attack roll.
        #Get Modifier
        c.execute("SELECT modifier FROM attacks WHERE name = ?", (name, ))
        recievedList = (c.fetchall())
        recievedTupple = recievedList[0]
        mod = int(str(recievedTupple[0]))

        #Get Damage Dice
        c.execute("SELECT damageDice FROM attacks WHERE name = ?", (name, ))
        recievedList = (c.fetchall())
        recievedTupple = recievedList[0]
        damageDice = int(str(recievedTupple[0]))

        #Get Added Damage
        c.execute("SELECT extraDamage FROM attacks WHERE name = ?", (name, ))
        recievedList = (c.fetchall())
        recievedTupple = recievedList[0]
        addedDamage = int(str(recievedTupple[0]))

    elif choice == "s":
        valid_name = False
        while not valid_name:
            try:
                name = input("What is the skill name?")
                c.execute("SELECT * FROM skills")
                valid_name = True
            except:
                print("Invalid skill name.")

        #Get Modifier
        c.execute("SELECT modifier FROM skills WHERE name = ?", (name, ))
        recievedList = (c.fetchall())
        recievedTupple = recievedList[0]
        mod = int(str(recievedTupple[0]))

        damageDice = 0
        addedDamage = 0

    else:
        assert False, "An invalid choice has been accepted in 'getInfo.' "

        #Add in the info.

    roll(name, mod, damageDice, addedDamage, choice)


##################################
#  Roll Function
##################################
def roll(name, mod, damageDice=0, addedDamage=0, choice="Error"):

    #If it's an attack roll.
    if choice == "a":
        #Roll to hit.
        toHitRoll = random.randrange(1, 21)
        # toHitRoll = 20
        toHit = toHitRoll + mod
        higherThanAc = input(f"Does {toHit} hit (y/n)? ")

        #Does it hit?
        if higherThanAc == "y" or toHitRoll == 20:
            damageDice = random.randrange(1, damageDice + 1)

            #If it's critical, then do more damage.
            if toHitRoll == 20:
                damage = damageDice + damageDice + addedDamage
                print(f"You did {damage} damage with that critical roll! ")
            else:
                damage = damageDice + addedDamage
                print(f"You did {damage} damage!")
        elif higherThanAc == "n":
            print("You missed! Try again on your next turn.")
        else:
            print("That's not a valid input.")

    #Skill roll.
    elif choice == "s":

        #Roll the check and compare it to the DC.
        try:
            dc = int(input("What is the DC required? (Number only) "))
            abilityRoll = 0
            abilityRoll = random.randrange(1, 21)
            abilityCheck = abilityRoll + mod

            print(f"Your total roll is : {abilityCheck}.")
            #If the ability succeeds and it didn't roll a nat 1.
            if abilityCheck >= dc and abilityRoll > 1:
                assert abilityRoll > 1, "Ability roll succeeded with a nat 1."
                if abilityRoll == 20:
                    print("There's no way you could fail with that nat 20.")
                else:
                    print("You succeeded your skill check! ")

            #If they failed their check.
            elif abilityCheck < dc and abilityRoll > 1:
                print("You failed your skill check. :(")
            #If they failed with a nat 1.
            if abilityRoll == 1 or abilityCheck <= 1:
                print("You failed in the worst possible way with that 1.")

        except:
            print("Please enter a valid input.")


##################################
# Main function
##################################

wantRoll = True

#Roll a skill or attack roll as long as wanted.
while wantRoll:
    #Want an attack or skill roll?
    choice = input("Rolling attack or skill? (a/s) ")
    if choice == 'a' or 's':
        getInfo(choice)

        #Check if done
        print("")
        done = input("Want to roll again? (y/n)")
        if done == "n":
            wantRoll = False
            print("Thanks for rolling!")

    #Error check
    else:
        print("Invalid Input, please try again.")

c.close()