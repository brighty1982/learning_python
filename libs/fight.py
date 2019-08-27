
# resolve a fight between the player and an enemy combatent
#-------------------------------------------------------------------
def resolve_combat(player, enemy, ambush):
    
    success = False

    # max +1 enemy initiative if it's an ambush to ensure they attack first
    if(ambush): enemy.initiative = 11

    # who attacks first
    if(player.initiative >= enemy.initiative):
        attacker = player
        defender = enemy
    else:
        attacker = enemy
        defender = player

    # resolve combat - fight until one oponent has 0 wounds remaining
    while True:
        
        print(attacker.name + " attacks!")

        if(check_to_hit(attacker.weapon_skill, defender_weapon_skill)):
            print("Successful hit!")
            if(check_armour_save(attacker.strength, defender.armour_save)):
                print("Armour blocks the blow!")
            else:
                if(check_to_wound(attacker.strength, defender.toughness)):
                    defender.wounds.subtract(1)
                    print("The hit has caused a wound!")
        else:
            print("The attack misses!")

        if(defender.wounds <= 0):
            if attacker == player: success = True
            break
        else: # swap attacker and defender and continue fight
            temp = attacker 
            attacker = defender
            defender = temp

    return success
#-------------------------------------------------------------------
