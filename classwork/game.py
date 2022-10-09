import random
import sys
######
max_pers_hp = 100
pers_hp = 100
pers_armor = 50
pers_max_hp = 100
pers_atk = 30
pers_heal = 10
####
enemy_max_hp = [100, 200, 300, 400, 500]
enemy_max_armor = [50, 60, 70, 80]
enemy_hp = random.choice(enemy_max_hp)
enemy_armor = random.choice(enemy_max_armor)
enemy_atack = random.randint(5, 35)
#######
def enemy_atacks():
    global pers_armor, enemy_atack, pers_hp
    print('Enemy deals ', enemy_atack, 'to you')
    if pers_armor != 0:
        if pers_armor - enemy_atack < 0:
            pers_armor = 0
        elif pers_armor - enemy_atack > 0:
            pers_armor = pers_armor - enemy_atack
        elif pers_armor - enemy_atack == 0:
            pers_armor = 0
        else:
            print('error, try restarting the game')
    if pers_armor == 0:
        pers_hp = pers_hp - enemy_atack
        if pers_hp <= 0:
            print('You lost')
            sys.exit()
def attack_enemy():
    global enemy_hp, enemy_armor, pers_atk
    if enemy_hp - pers_atk > 0:
        enemy_hp = enemy_hp - pers_atk
    elif enemy_hp - pers_atk <= 0:
        print('You won!')
        sys.exit()
    else:
        print('Error')

def heal():
    global pers_hp, max_pers_hp
    if pers_heal + pers_hp >= 100:
        pers_hp = 100
    elif pers_heal + pers_hp < 100:
        pers_hp = pers_hp + pers_heal
def wait():
    global pers_heal, pers_atk
    pers_heal = pers_heal + 10
    pers_atk = pers_atk + 10
def renew():
    global pers_hp, pers_armor, enemy_hp, enemy_armor

##################################

while enemy_hp > 0:
    print('-----------------------------------------------------')
    print('Enemy has: ', enemy_hp, 'hp, and', enemy_armor, 'armor')
    print('what do you want to do? 1- hit by', pers_atk, ';2- heal by', pers_heal,
          ';3- wait one turn to heal and damage by 10 more')
    print('Your hp: ', pers_hp, 'your armor: ', pers_armor)
    choice = int(input())
    if choice == 1:
        attack_enemy()
        renew()
        enemy_atacks()
    elif choice == 2:
        heal()
        renew()
        enemy_atacks()
    elif choice == 3:
        renew()
        wait()
        enemy_atacks()
if enemy_hp <= 0:
    print('You won!')
