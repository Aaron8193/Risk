import random
import math

def riskFight(attackUnits, defenseUnits):
    firstBattle = 1
    secondBattle = 1
    battle = 0
    newAttackUnits = attackUnits
    newDefenseUnits = defenseUnits
    if attackUnits >= 4:
        attackRoll1 = random.randint(1, 6)
        attackRoll2 = random.randint(1, 6)
        attackRoll3 = random.randint(1, 6)
    elif attackUnits == 3:
        attackRoll1 = random.randint(1, 6)
        attackRoll2 = random.randint(1, 6)
        attackRoll3 = 0
    elif attackUnits == 2:
        attackRoll1 = random.randint(1, 6)
        attackRoll2 = 0
        attackRoll3 = 0
    else:
        return "The amount of attacking troops is invalid. Please try again."
    if defenseUnits >= 2:
        defenseRoll1 = random.randint(1, 6)
        defenseRoll2 = random.randint(1, 6)
    elif defenseUnits == 1:
        defenseRoll1 = random.randint(1, 6)
        defenseRoll2 = 0
    else:
        return "The amount of defending troops is invalid. Please try again."
    print "The first attack die rolled gave a", attackRoll1,"!"
    if attackUnits >= 3:
        print "The second attack die rolled gave a", attackRoll2,"!"
        if attackUnits>= 4:
            print "The third attack die rolled gave a", attackRoll3,"!"
    print "The first defense die rolled gave a", defenseRoll1,"!"
    if defenseUnits >= 2:
        print "The second defense die rolled a", defenseRoll2,"!"
    if attackUnits >= 4:
        if attackRoll1 >= attackRoll2 >= attackRoll3:
            firstAttack = attackRoll1
            secondAttack = attackRoll2
        elif attackRoll1 >= attackRoll3 >= attackRoll2:
            firstAttack = attackRoll1
            secondAttack = attackRoll3 
        elif attackRoll2 >= attackRoll1 >= attackRoll3:
            firstAttack = attackRoll2 
            secondAttack = attackRoll1 
        elif attackRoll2 >= attackRoll3 >= attackRoll1:
            firstAttack = attackRoll2
            secondAttack = attackRoll3
        elif attackRoll3 >= attackRoll1 >= attackRoll2:
            firstAttack = attackRoll3
            secondAttack = attackRoll1
        elif attackRoll3 >= attackRoll2 >= attackRoll1:
            firstAttack = attackRoll3
            secondAttack = attackRoll2
        else:
            return "The calculations have been thrown off through unknown means. Please try again"
        print "The two highest rolls from attack were", firstAttack,"and",secondAttack,"!"
    elif attackUnits == 3:
        if attackRoll1 >= attackRoll2:
            firstAttack = attackRoll1 
            secondAttack = attackRoll2
        elif attackRoll2 >= attackRoll1:
            firstAttack = attackRoll2 
            secondAttack = attackRoll1 
        else:
            return "The calculations have been thrown off through unknown means. Please try again"
        print "The two highest rolls from attack were", firstAttack,"and",secondAttack,"!"
    elif attackUnits == 2:
        firstAttack = attackRoll1
        print "The highest roll from attack was", firstAttack,"!"
    if defenseUnits >= 2:
        if defenseRoll1 >= defenseRoll2:
               firstDefense = defenseRoll1
               secondDefense = defenseRoll2
        elif defenseRoll2 >= defenseRoll1:
               firstDefense = defenseRoll2
               secondDefense = defenseRoll1
        else:
            return "The calculations have been thrown off through unknown means. Please try again"
        print "The two highest rolls from defense were", firstDefense,"and", secondDefense, "!"
    elif defenseUnits == 1:
        firstDefense = defenseRoll1
        secondDefense = 0
        print "The highest roll from defense was", firstDefense, "!"
    else:
        return "The calculations have been thrown off through unknown means. Please try again"
    if battleChecker(firstAttack, firstDefense) is True:
        newAttackUnits += -1
    else:
        newDefenseUnits += -1
    if battleChecker(secondAttack, secondDefense) is True:
        newAttackUnits += -1
    else:
        newDefenseUnits += -1
    print "Offense has", newAttackUnits, "armies left!"
    print "Defense has", newDefenseUnits, "armies left!"
def battleChecker(attack, defense):
    battle = 0
    if attack > defense:
        battle += 1
    elif attack <= defense:
        battle += 2
    else:
        battle == 0
    if battle == 1:
        print "One battle is won by attack, with a", attack, "from attack and", defense, "from defense!"
        return False
    elif battle == 2:
        print "One battle is won by defense, with a", attack, "from attack and", defense, "from defense!"
        return True
    else:
        return 'No one wins'
def battleCheckerlesstext(attack, defense):
    battle = 0
    if attack > defense:
        battle += 1
    elif attack <= defense:
        battle += 2
    else:
        battle == 0
    if battle == 1:
        return False
    elif battle == 2:
        return True
    else:
        return 'No one wins'
def riskRefight(attackUnits, defenseUnits):
    if attackUnits == 1:
        if defenseUnits == 1:
            print "Defense has successfully held their ground, with only", defenseUnits, "army left!"
        else:
            print "Defense has successfully held their ground, with only", defenseUnits, "armies left!"
            return "Defense Wins"
    elif defenseUnits == 0:
        print "Attack has successfully conquered the defense, with", attackUnits, "armies to spare!"
        return "Attack Wins"
    else:
        return True
def riskRefightlesstext(attackUnits, defenseUnits):
    if attackUnits == 1:
        newDefenseUnits = defenseUnits
        return "Defense Wins"
    elif defenseUnits == 0:
        newAttackUnits = defenseUnits
        return "Attack Wins"
    else:
        return True
    
def riskInfiniteFight(attackUnits, defenseUnits):
    newAttackUnits = attackUnits
    newDefenseUnits = defenseUnits
    while riskRefight(newAttackUnits, newDefenseUnits) is True:
        newAttackUnits = newAttackUnits
        newDefenseUnits = newDefenseUnits
        if attackUnits >= 4:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = random.randint(1, 6)
            attackRoll3 = random.randint(1, 6)
        elif attackUnits == 3:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = random.randint(1, 6)
            attackRoll3 = 0
        elif attackUnits == 2:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = 0
            attackRoll3 = 0
        else:
            return "The amount of attacking troops is invalid. Please try again."
        if defenseUnits >= 2:
            defenseRoll1 = random.randint(1, 6)
            defenseRoll2 = random.randint(1, 6)
        elif defenseUnits == 1:
            defenseRoll1 = random.randint(1, 6)
            defenseRoll2 = 0
        else:
            return "The amount of defending troops is invalid. Please try again."
        print "The first attack die rolled gave a", attackRoll1,"!"
        if attackUnits >= 3:
            print "The second attack die rolled gave a", attackRoll2,"!"
            if attackUnits>= 4:
                  print "The third attack die rolled gave a", attackRoll3,"!"
        print "The first defense die rolled gave a", defenseRoll1,"!"
        if defenseUnits >= 2:
            print "The second defense die rolled a", defenseRoll2,"!"
        if attackUnits >= 4:
            if attackRoll1 >= attackRoll2 >= attackRoll3:
                firstAttack = attackRoll1
                secondAttack = attackRoll2
            elif attackRoll1 >= attackRoll3 >= attackRoll2:
                firstAttack = attackRoll1
                secondAttack = attackRoll3 
            elif attackRoll2 >= attackRoll1 >= attackRoll3:
                firstAttack = attackRoll2 
                secondAttack = attackRoll1 
            elif attackRoll2 >= attackRoll3 >= attackRoll1:
                firstAttack = attackRoll2
                secondAttack = attackRoll3
            elif attackRoll3 >= attackRoll1 >= attackRoll2:
                firstAttack = attackRoll3
                secondAttack = attackRoll1
            elif attackRoll3 >= attackRoll2 >= attackRoll1:
                firstAttack = attackRoll3
                secondAttack = attackRoll2
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
            print "The two highest rolls from attack were", firstAttack,"and",secondAttack,"!"
        elif attackUnits == 3:
            if attackRoll1 >= attackRoll2:
                firstAttack = attackRoll1 
                secondAttack = attackRoll2
            elif attackRoll2 >= attackRoll1:
                firstAttack = attackRoll2 
                secondAttack = attackRoll1 
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
            print "The two highest rolls from attack were", firstAttack,"and",secondAttack,"!"
        elif attackUnits == 2:
            firstAttack = attackRoll1
            print "The highest roll from attack was", firstAttack,"!"
        if defenseUnits >= 2:
            if defenseRoll1 >= defenseRoll2:
                   firstDefense = defenseRoll1
                   secondDefense = defenseRoll2
            elif defenseRoll2 >= defenseRoll1:
                   firstDefense = defenseRoll2
                   secondDefense = defenseRoll1
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
            print "The two highest rolls from defense were", firstDefense,"and", secondDefense, "!"
        elif defenseUnits == 1:
            firstDefense = defenseRoll1
            secondDefense = 0
            print "The highest roll from defense was", firstDefense, "!"
        else:
            return "The calculations have been thrown off through unknown means. Please try again"
        if battleChecker(firstAttack, firstDefense) is True:
            newAttackUnits += -1
        else:
            newDefenseUnits += -1
        if secondDefense != 0 and newDefenseUnits != 0:
            if battleChecker(secondAttack, secondDefense) is True:
                newAttackUnits += -1
            else:
                newDefenseUnits += -1
        if newAttackUnits == 1:
            print "Offense has", newAttackUnits, "army left!"
        else:
            print "Offense has", newAttackUnits, "armies left!"
        if newDefenseUnits == 1:
            print "Defense has", newDefenseUnits, "army left!"
        else:
            print "Defense has", newDefenseUnits, "armies left!"
    else:
        return 'The battle has ended!'
def riskInfiniteFightlesstext(attackUnits, defenseUnits):
    remainingDefenseUnits = 0
    remainingAttackUnits = 0
    newAttackUnits = attackUnits
    newDefenseUnits = defenseUnits
    while riskRefightlesstext(newAttackUnits, newDefenseUnits) is True:
        newAttackUnits = newAttackUnits
        newDefenseUnits = newDefenseUnits
        if attackUnits >= 4:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = random.randint(1, 6)
            attackRoll3 = random.randint(1, 6)
        elif attackUnits == 3:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = random.randint(1, 6)
            attackRoll3 = 0
        elif attackUnits == 2:
            attackRoll1 = random.randint(1, 6)
            attackRoll2 = 0
            attackRoll3 = 0
        else:
            return "The amount of attacking troops is invalid. Please try again."
        if defenseUnits >= 2:
            defenseRoll1 = random.randint(1, 6)
            defenseRoll2 = random.randint(1, 6)
        elif defenseUnits == 1:
            defenseRoll1 = random.randint(1, 6)
            defenseRoll2 = 0
        else:
            return "The amount of defending troops is invalid. Please try again."
        if attackUnits >= 4:
            if attackRoll1 >= attackRoll2 >= attackRoll3:
                firstAttack = attackRoll1
                secondAttack = attackRoll2
            elif attackRoll1 >= attackRoll3 >= attackRoll2:
                firstAttack = attackRoll1
                secondAttack = attackRoll3 
            elif attackRoll2 >= attackRoll1 >= attackRoll3:
                firstAttack = attackRoll2 
                secondAttack = attackRoll1 
            elif attackRoll2 >= attackRoll3 >= attackRoll1:
                firstAttack = attackRoll2
                secondAttack = attackRoll3
            elif attackRoll3 >= attackRoll1 >= attackRoll2:
                firstAttack = attackRoll3
                secondAttack = attackRoll1
            elif attackRoll3 >= attackRoll2 >= attackRoll1:
                firstAttack = attackRoll3
                secondAttack = attackRoll2
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
        elif attackUnits == 3:
            if attackRoll1 >= attackRoll2:
                firstAttack = attackRoll1 
                secondAttack = attackRoll2
            elif attackRoll2 >= attackRoll1:
                firstAttack = attackRoll2 
                secondAttack = attackRoll1 
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
        elif attackUnits == 2:
            firstAttack = attackRoll1
            secondAttack = 0
        if defenseUnits >= 2:
            if defenseRoll1 >= defenseRoll2:
                   firstDefense = defenseRoll1
                   secondDefense = defenseRoll2
            elif defenseRoll2 >= defenseRoll1:
                   firstDefense = defenseRoll2
                   secondDefense = defenseRoll1
            else:
                return "The calculations have been thrown off through unknown means. Please try again"
        elif defenseUnits == 1:
            firstDefense = defenseRoll1
            secondDefense = 0
        else:
            return "The calculations have been thrown off through unknown means. Please try again"
        if battleCheckerlesstext(firstAttack, firstDefense) is True:
            newAttackUnits += -1
        else:
            newDefenseUnits += -1
        if secondDefense != 0 and newDefenseUnits != 0:
            if battleCheckerlesstext(secondAttack, secondDefense) is True:
                newAttackUnits += -1
            else:
                newDefenseUnits += -1
    else:
        if newAttackUnits == 1:
            remainingDefenseUnits += newDefenseUnits
            return True
        elif newDefenseUnits == 0:
            remainingAttackUnits += newAttackUnits
            return False
        else:
            return 0
        
def probability(tries, newAttackUnits, newDefenseUnits):
    attempts = 0
    attackWins = 0
    defenseWins = 0
    attackTroops = 0
    defenseTroops = 0
    remainingAttackUnits = 0
    remainingDefenseUnits = 0
    while tries > attempts:
        if riskInfiniteFightlesstext(newAttackUnits, newDefenseUnits) is True:
            defenseWins += 1
            defenseTroops += remainingDefenseUnits
        elif riskInfiniteFightlesstext(newAttackUnits, newDefenseUnits) is False:
            attackWins += 1
            attackTroops += remainingAttackUnits
        else:
            attempts += -1
        attempts += 1
    attackWinRatio = attackWins / float(tries)
    defenseWinRatio = defenseWins / float(tries)
    attackTroopRatio = attackTroops / float(attackWins)
    defenseTroopRatio = defenseTroops / float(defenseWins)
    print "The attacking side, with", newAttackUnits,"armies won", attackWins, "out of", tries, "battles. This equates to a victory ratio of", attackWinRatio,"! In addition, they averaged", attackTroopRatio, "troops remaining after victory!"
    print "The defending side, with", newDefenseUnits,"armies, won", defenseWins, "out of", tries, "battles. This equates to a victory ratio of", defenseWinRatio,"! In addition, they averaged", defenseTroopRatio, "troops remaining after victory!"
probability(1000, 3, 2)

    
