from random import randint
import Classes

def move(entity = Classes.Entity, target = Classes.Entity):
    res = int(input("Put here the dialogue for choosing a move"))

    if res == 1:
        target.he - (entity.att - target.de)
    elif res == 2:
        if entity.isEnemy:
            target.he - (entity.att - target.de)
        else:
            Classes.despawn(target)




def EnterCombatMode(entity = Classes.Entity, target = Classes.Entity):
    if not target.CombatMode and entity.CombatMode:

        try:
            entity.health = 100 + entity.armour.he
        except:
            pass
        try:
            entity.att += entity.armour.att
        except:
            pass
        try:
            entity.att += entity.weapon.att
        except:
            pass
        try:
            entity.de += entity.weapon.de
        except:
            pass
        try:
            entity.de += entity.armour.de
        except:
            pass


        try:
            target.health = 100 + entity.armour.he
        except:
            pass
        try:
            target.att += target.armour.att
        except:
            pass
        try:
            target.att+= target.weapon.att
        except:
            pass
        try:
            target.de += target.weapon.de
        except:
            pass
        try:
            target.de += target.armour.de
        except:
            pass

        entity.CombatMode = True
        target.CombatMode = True

        mov = None

        while (target.he > 0 or entity.he > 0):
            if mov is None:
                if randint(1, 2) == 1:
                    mov = entity
                else:
                    mov = target
            if mov == target:
                move(target, entity)
            else:
                move(entity, target)
        