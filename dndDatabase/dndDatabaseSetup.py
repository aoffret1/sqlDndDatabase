import sqlite3
# import pragma

#Connect method
conn = sqlite3.connect('dndDB.db')


#Executes SQL commands.
c = conn.cursor()

# c.execute("PRAGMA table_info('skills')").fetchall()

#Make the table
# c.execute("CREATE TABLE skills (id INTEGER, name TEXT, modifier INTEGER)")
# c.execute("DROP TABLE skills")

# """CREATE SKILLS TABLE """

def insert_skill_info(id, name, mod):
    with conn:
        c.execute("INSERT INTO skills VALUES( ?, ?, ?)", 
        (id, name, mod,))

# def delete_skill(name):
#     with conn:
#         c.execute("DELETE FROM skills WHERE name = :name", (name,))


# #Print what's in database
print("Skills Table: ")
c.execute("SELECT * FROM skills")
print(c.fetchall())



#Keep adding skills until they are all in.
have_more = True
id = 1
while have_more:
    
    name = input("What is the skill name? ")
    mod = int(input("What is the modifier? "))
    insert_skill_info(id, name, mod)

#     # delete_skill("test")

    #Are you done?
    done = input("Are you done? (y/n")
    id = id + 1
    if done == 'y':
        have_more = False


#Create attack roll table
# c.execute("DROP TABLE attacks")
# c.execute("CREATE TABLE attacks (id INTEGER, name TEXT, modifier INTEGER, damageDice INT, extraDamage INT)")

def insert_attack_info(id, name, mod, dice, damageMod):
    with conn:
        c.execute("INSERT INTO attacks VALUES( ?, ?, ?, ?, ?)", 
        (id, name, mod, dice, damageMod,))

# # def delete_attack(name):
# #     with conn:
# #         c.execute("DELETE FROM attacks WHERE name = :name", (name,))

print("\n\nAttack Table")
c.execute("SELECT * FROM attacks")
print(c.fetchall())

have_more = True
id = 1
while have_more:
    name = input("What is the attack name? ")
    mod = int(input("What is the modifier? "))
    dice = int(input("How big is the damage dice? "))
    damageMod = int(input("What is the damage added on? "))

    insert_attack_info(id, name, mod, dice, damageMod)
    id = id + 1
#     #Are you done?
    done = input("Are you done? (y/n")
    if done == 'y':
        have_more = False

c.close()
# #Come up with pseudocode for stuff



