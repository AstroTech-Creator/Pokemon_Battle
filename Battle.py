import random
import sys
import time


# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

class Pokemon:
    def __init__(self, name, type1, type2, level, moves, base):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.moves = moves
        self.level = level
        self.money = 100
        self.Pokeball = 5
        self.Ultraball = 0
        self.Greatball = 0
        
        # Base Stats
        self.base_hp = base['HP']
        self.base_attack = base['Attack']
        self.base_defense = base['Defense']
        self.base_spatk = base['SpAtk']
        self.base_spdef = base['SpDef']
        self.base_speed = base['Speed']
        self.base_total = base['Total']
        self.base_exp = base['Exp']
        
        # IV Stats
        self.iv_hp = random.randint(1,31)
        self.iv_attack = random.randint(1,31)
        self.iv_defense = random.randint(1,31)
        self.iv_spatk = random.randint(1,31)
        self.iv_spdef = random.randint(1,31)
        self.iv_speed = random.randint(1,31)

        # EV Stats
        self.ev_hp = 0
        self.ev_attack = 0
        self.ev_defense = 0
        self.ev_spatk = 0
        self.ev_spdef = 0
        self.ev_speed = 0

        # Main Stats
        # HP Stats = ((2 * base + iv + ev / 4) * level / 100) + level + 10
        # Other stats = ((2 * base + iv + ev / 4) * level / 100) + 5 * Nature Value
        self.Poke_hp = int(((2*self.base_hp+self.iv_hp+self.ev_hp/4)*self.level/100)+self.level+10)
        self.Poke_attack = int(((2*self.base_attack+self.iv_attack+self.ev_attack/4)*self.level/100)+5)
        self.Poke_defense = int(((2*self.base_defense+self.iv_defense+self.ev_defense/4)*self.level/100)+5)
        self.Poke_spatk = int(((2*self.base_spatk+self.iv_spatk+self.ev_spatk/4)*self.level/100)+5)
        self.Poke_spdef = int(((2*self.base_spdef+self.iv_spdef+self.ev_spdef/4)*self.level/100)+5)
        self.Poke_speed = int(((2*self.base_speed+self.iv_speed+self.ev_speed/4)*self.level/100)+5)
        self.Poke_exp = int(self.level**3)

        # Pokemon list
        self.my_poke = [self.name]


    # Set Stats Of Wild Pokemon After Come random_level Wild Pokemon
    def Random_stat(self, Random_Poke):
        Random_Poke.level = random.randint(1, 100)
        Random_Poke.Poke_hp = int(((2*Random_Poke.base_hp+Random_Poke.iv_hp+Random_Poke.ev_hp/4)*Random_Poke.level/100)+Random_Poke.level+10)
        Random_Poke.Poke_attack = int(((2*Random_Poke.base_attack+Random_Poke.iv_attack+Random_Poke.ev_attack/4)*Random_Poke.level/100)+5)
        Random_Poke.Poke_defense = int(((2*Random_Poke.base_defense+Random_Poke.iv_defense+Random_Poke.ev_defense/4)*Random_Poke.level/100)+5)
        Random_Poke.Poke_spatk = int(((2*Random_Poke.base_spatk+Random_Poke.iv_spatk+Random_Poke.ev_spatk/4)*Random_Poke.level/100)+5)
        Random_Poke.Poke_spdef = int(((2*Random_Poke.base_spdef+Random_Poke.iv_spdef+Random_Poke.ev_spdef/4)*Random_Poke.level/100)+5)
        Random_Poke.Poke_speed = int(((2*Random_Poke.base_speed+Random_Poke.iv_speed+Random_Poke.ev_speed/4)*Random_Poke.level/100)+5)
        Random_Poke.Poke_exp = int(Random_Poke.level**3)


    # Just Show Our Pokemon Name and Level At 1st time
    def choose(self):
        delay_print(f"You Choose {self.name}")
        delay_print(f"\nYour Pokemon level is {self.level} and helth is {self.Poke_hp}")
        time.sleep(0.5)
        self.random_level()

    
    # Come Random Level Wild Pokemon
    def random_level(self):
        All_Poke = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise]
        Random_Poke = random.choice(All_Poke)
        self.Random_stat(Random_Poke)

        if self.level <= 10:
            if Random_Poke.level <=10 :
                self.hunt(Random_Poke)
            else:
                self.random_level()

        elif self.level <=25:
            if Random_Poke.level <=25 :
                self.hunt(Random_Poke)
            else:
                self.random_level()

        elif self.level <= 50:
            if Random_Poke.level <=50:
                self.hunt(Random_Poke)
            else:
                self.random_level()

        else :
            if Random_Poke.level <=100 :
                self.hunt(Random_Poke)
            else:
                self.random_level()


    # You Hunt Wild Pokemon And Pokemon Come Throw random_level Function 
    def hunt(self, Random_Poke):
        action = input("\n\nYou want to hunt pokemon [y/n]: ")
        action = action.lower()
        if action=="y":
            delay_print(f"A wild {Random_Poke.name} has appeared")
            delay_print(f"\nlevel is {Random_Poke.level} and helth is {Random_Poke.Poke_hp}")
            time.sleep(0.5)
            self.hunt_choise(Random_Poke)
        elif action=="n":
            self.save_game()
        else:
            print("Enter valid input")
            self.hunt(Random_Poke)


    # You Have Option For Battle Or Run
    def hunt_choise(self, Random_Poke):
        action = input("\n\nYou want to battle or run from pokemon  [b/r]: ")
        action = action.lower()
        if action=="b":
            self.choose_move(Random_Poke)
        elif action=="r":
            delay_print(f"You run from wild {Random_Poke.name}")
            self.random_level()
        else:
            print("Enter valid input")
            self.hunt_choise(Random_Poke)


    # For adding speed counter go to hunt_choise and after choose 'b' set self.Speed_count(Random_Poke)

    # More Speed Pokemon Move 1st
    # def Speed_count(self, Random_Poke):
    #     if self.Poke_speed >= Random_Poke.Poke_speed:
    #         self.choose_move(Random_Poke)
    #     else:
    #         delay_print(f"\n{Random_Poke.name} move first because its fast")
    #         self.computer_turn(Random_Poke)

    
    # Our Turn For Choose Move
    def choose_move(self, Random_Poke):
        try:
            print(f"\nYour turn choose attack")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            print("5. Your Pokemon")
            print("6. Check your bag")
            print("7. Shop")
            print("8. Run From Wild Pokemon")

            index = int(input('Pick a move: '))
            if 0<index<=4:
                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                Random_Poke_damage = int(self.Poke_attack*(100/(100+Random_Poke.Poke_defense)))
                Random_Poke.Poke_hp -= Random_Poke_damage
                print(f"\n{Random_Poke.name} get {Random_Poke_damage} damage")
                
                if Random_Poke.Poke_hp <= 0:
                    delay_print(f"The wild {Random_Poke.name} fainted")
                    self.ExpCount(Random_Poke)
                else:
                    print(f"Now {Random_Poke.name} have {Random_Poke.Poke_hp} HP left")
                    self.computer_turn(Random_Poke)

            elif index == 5:
                Poke_list = ", ".join(self.my_poke)
                print(f"\nYour pokemons : {Poke_list}")
                self.choose_move(Random_Poke)

            elif index == 6:
                self.bag(Random_Poke)   

            elif index == 7:
                self.Shop(Random_Poke)

            elif index == 8:
                delay_print(f"\nYou run away from wild {Random_Poke.name}")
                self.ExpCount(Random_Poke)

            else :
                print("Wrong input")
                self.choose_move(Random_Poke)
            time.sleep(0.5)

        except ValueError as e:
            print("Wrong input, only number allow")
            self.choose_move(Random_Poke)
            time.sleep(0.5)


    # Commputer Turn For Choose Move
    def computer_turn(self, Random_Poke):
        #for attack computer turn
        print(f"\n{Random_Poke.name}'s turn")
        random_move = random.choice(Random_Poke.moves)
        delay_print(f"{Random_Poke.name} used {random_move}!")

        self_damage = int(Random_Poke.Poke_attack*(100/(100+self.Poke_defense)))
        self.Poke_hp -= self_damage
        print(f"\n{self.name} get {self_damage} damage")
        time.sleep(0.5)

        if self.Poke_hp <= 0:
            delay_print(f"Your {self.name} fainted")
            self.ExpCount(Random_Poke)
        else:
            print(f"Now Your {self.name} have {self.Poke_hp} HP left")
            self.choose_move(Random_Poke)

    
    # Experience of Our Pokemon After Finish Battle
    def ExpCount(self, Random_Poke):
        # exp = floor(floor(√(A)*(A*A))*B/floor(√(C)*(C*C)))+1
        # Exp_gain = (int(int((A**0.5)*(A*A))*B/int((C**0.5)*(C*C)))+1)
        # value A is (OpponentLevel * 2) + 10
        # Value B is (OpponentBaseExperience * OpponentLevel / 5)
        # Value C is (OpponentLevel + UserLevel + 10)

        Random_Poke_MaxHp = int(((2*Random_Poke.base_hp+Random_Poke.iv_hp+Random_Poke.ev_hp/4)*Random_Poke.level/100)+Random_Poke.level+10)
        if Random_Poke.Poke_hp <= 0:
            A = (Random_Poke.level * 2) + 10
            B = (Random_Poke.base_exp * Random_Poke.level / 5)
            C = (Random_Poke.level + self.level + 10)
            Exp_gain = (int(int((A ** 0.5) * (A * A)) * B / int((C ** 0.5) * (C * C))) + 1)
            self.money += (int(self.level/10)+5)
            delay_print(f"\nYou get {Exp_gain} Exp and {int(self.level/10)+5} coin")
            self.Poke_exp += Exp_gain
            # delay_print(f"\nNow Total Exp is {self.Poke_exp}")
            # print(f"\nYour total money: {self.money}")

        elif Random_Poke.Poke_hp == Random_Poke_MaxHp:
            pass

        elif Random_Poke.Poke_hp >= Random_Poke_MaxHp/2 :
            A = (Random_Poke.level * 2) + 10
            B = (Random_Poke.base_exp * Random_Poke.level / 5)
            C = (Random_Poke.level + self.level + 10)
            Exp_gain = int(((int((A ** 0.5) * (A * A)) * B / int((C ** 0.5) * (C * C))) + 1)/4)
            delay_print(f"\nYou get {Exp_gain} Exp")
            self.Poke_exp += Exp_gain

        elif Random_Poke.Poke_hp < Random_Poke_MaxHp/2 :
            A = (Random_Poke.level * 2) + 10
            B = (Random_Poke.base_exp * Random_Poke.level / 5)
            C = (Random_Poke.level + self.level + 10)
            Exp_gain = int(((int((A ** 0.5) * (A * A)) * B / int((C ** 0.5) * (C * C))) + 1)/2)
            delay_print(f"\nYou get {Exp_gain} Exp")
            self.Poke_exp += Exp_gain

        if self.Poke_exp >= (self.level+1)**3:
            delay_print(f"\nYour {self.name} is level up")
            time.sleep(0.5)
            self.levelup()

        # Helth recover
        self.Poke_hp = int(((2*self.base_hp+self.iv_hp+self.ev_hp/4)*self.level/100)+self.level+10)
        Random_Poke.Poke_hp = int(((2*Random_Poke.base_hp+Random_Poke.iv_hp+Random_Poke.ev_hp/4)*Random_Poke.level/100)+Random_Poke.level+10)
        self.random_level()


    # Levelup Our Pokemon After Calculate Experience 
    def levelup(self):
        self.level += 1
        self.Poke_hp = int(((2*self.base_hp+self.iv_hp+self.ev_hp/4)*self.level/100)+self.level+10)
        self.Poke_attack = int(((2*self.base_attack+self.iv_attack+self.ev_attack/4)*self.level/100)+5)
        self.Poke_defense = int(((2*self.base_defense+self.iv_defense+self.ev_defense/4)*self.level/100)+5)
        self.Poke_spatk = int(((2*self.base_spatk+self.iv_spatk+self.ev_spatk/4)*self.level/100)+5)
        self.Poke_spdef = int(((2*self.base_spdef+self.iv_spdef+self.ev_spdef/4)*self.level/100)+5)
        self.Poke_speed = int(((2*self.base_speed+self.iv_speed+self.ev_speed/4)*self.level/100)+5)
        print(f"\nYou {self.name} level is {self.level} and helth is {self.Poke_hp}")


    # Shop For Buy Pokeballs 
    def Shop(self, Random_Poke):
        delay_print("\nWelcome to the Shop")
        time.sleep(0.5)
        print(f"\nYou have {self.money} coin")
        print(f"Pokeball - 10 coin \nGreatball - 20 coin \nUltraball - 40 coin \nWrite 'B' for go back to battle")

        action = input("\nEnter ball name: ")
        action = action.replace(" ", "")
        action = action.lower()
        if action == "pokeball" or action == "greatball" or action == "ultraball":
            try:
                count = int(input("Enter number of ball: "))
                if action == "pokeball":
                    coin = count*10
                    if self.money >= coin:
                        self.money -= coin
                        self.Pokeball += count
                        delay_print(f"\nYou buy {count} pokeball")
                        delay_print(f"\nNow you left {self.money} coin\n")
                        self.choose_move(Random_Poke)
                    else:
                        delay_print("\nYou don't have enough coin\n")
                        self.Shop(Random_Poke)

                elif action == "greatball":
                    coin = count*20
                    if self.money >= coin:
                        self.money -= coin
                        self.Greatball += count
                        delay_print(f"\nYou buy {count} Greatball")
                        delay_print(f"\nNow you left {self.money} coin\n")
                        self.choose_move(Random_Poke)
                    else:
                        delay_print("You don't have enough coin\n")
                        self.Shop(Random_Poke)

                elif action == "ultraball":
                    coin = count*40
                    if self.money >= coin:
                        self.money -= coin
                        self.Ultraball += count
                        delay_print(f"\nYou buy {count} Ultraball")
                        delay_print(f"\nNow you left {self.money} coin\n")
                        self.choose_move(Random_Poke)
                    else:
                        delay_print("You don't have enough coin\n")
                        self.Shop(Random_Poke)

            except ValueError as e:
                delay_print("Wrong input, only number allow\n")
                self.Shop(Random_Poke)
                time.sleep(0.5)

        elif action == "b":
            time.sleep(1)
            self.choose_move(Random_Poke)

        else:
            delay_print("Wrong input\n")
            self.Shop(Random_Poke)


    # Bag for view Pokeballs and Catch Pokemon
    def bag(self, Random_Poke):
        delay_print(f"\nYou have {self.Pokeball} Poke ball, {self.Greatball} Great ball and {self.Ultraball} Ultra ball ")
        action = input(f"\nYou want to use Poke ball to catch pokemon or return to battle[p/b]: ")
        action = action.lower()
        if action == 'p':
            if self.Pokeball > 0:
                delay_print("You throw poke ball")
                slow_print("\n . . .")
                delay_print(f"\nYou catch wild {Random_Poke.name}")
                self.money += 10
                self.my_poke.append(Random_Poke.name)

                # Poke_list = ", ".join(self.my_poke)
                # time.sleep(0.5)
                # print(f"\nYour pokemons : {Poke_list}")

            else:
                delay_print(f"\nYou don't have any Poke ball")

            self.Pokeball -= 1
            self.random_level()

        elif action == 'b':
            self.choose_move(Random_Poke)
        else:
            print("Wrong input")
            self.bag(Random_Poke)

    # Save Game 
    def save_game(self):
        action = input('\nYou want to save game or not [y/n]: ')
        action = action.lower()
        if action == "y":
            time.sleep(0.5)
            delay_print("\nYour game is save and You exit game")
        elif action == "n":
            time.sleep(0.5)
            delay_print("\nYour game is not save and you exit game")
        else:
            print("Wrong input")
            time.sleep(0.5)
            self.save_game()

# Your 1st pokemon
Main_Bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Poison', 5, ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'HP':45, 'Attack':49, 'Defense':49, 'SpAtk':65, 'SpDef':65, 'Speed':45, 'Total':318, 'Exp':64})
Main_Charmander = Pokemon('Charmander', 'Fire', '', 5, ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'HP':39, 'Attack':52, 'Defense':43, 'SpAtk':60, 'SpDef':50, 'Speed':65, 'Total':309, 'Exp':62})
Main_Squirtle = Pokemon('Squirtle', 'Water', '', 5, ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'HP':44, 'Attack':48, 'Defense':65, 'SpAtk':50, 'SpDef':64, 'Speed':43, 'Total':314, 'Exp':63})

# Other pokemon data
Bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Poison', random.randint(1, 100), ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'HP':45, 'Attack':49, 'Defense':49, 'SpAtk':65, 'SpDef':65, 'Speed':45, 'Total':318, 'Exp':64})
Ivysaur = Pokemon('Ivysaur', 'Grass', 'Poison', random.randint(1, 100), ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'], {'HP':60, 'Attack':62, 'Defense':63, 'SpAtk':80, 'SpDef':80, 'Speed':60, 'Total':405, 'Exp':142})
Venusaur = Pokemon('Venusaur', 'Grass', 'Poison', random.randint(1, 100), ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'HP':80, 'Attack':82, 'Defense':83, 'SpAtk':100, 'SpDef':100, 'Speed':80, 'Total':525, 'Exp':263})

Charmander = Pokemon('Charmander', 'Fire', '', random.randint(1, 100), ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'HP':39, 'Attack':52, 'Defense':43, 'SpAtk':60, 'SpDef':50, 'Speed':65, 'Total':309, 'Exp':62})
Charmeleon = Pokemon('Charmeleon', 'Fire', '', random.randint(1, 100), ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'HP':58, 'Attack':64, 'Defense':58, 'SpAtk':80, 'SpDef':65, 'Speed':80, 'Total':405, 'Exp':142})
Charizard = Pokemon('Charizard', 'Fire', 'Flying', random.randint(1, 100), ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'HP':78, 'Attack':84, 'Defense':78, 'SpAtk':109, 'SpDef':85, 'Speed':10, 'Total':534, 'Exp':267})

Squirtle = Pokemon('Squirtle', 'Water', '', random.randint(1, 100), ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'HP':44, 'Attack':48, 'Defense':65, 'SpAtk':50, 'SpDef':64, 'Speed':43, 'Total':314, 'Exp':63})
Wartortle = Pokemon('Wartortle', 'Water', '', random.randint(1, 100), ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], {'HP':59, 'Attack':63, 'Defense':80, 'SpAtk':65, 'SpDef':80, 'Speed':58, 'Total':405, 'Exp':142})
Blastoise = Pokemon('Blastoise', 'Water', '', random.randint(1, 100), ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'HP':79, 'Attack':83, 'Defense':100, 'SpAtk':85, 'SpDef':105, 'Speed':78, 'Total':530, 'Exp':265})



# Choose first Pokemon
def first_choose():
    print ("Choose Your 1st Pokemon : \n1. Bulbasaur \n2. Charmander \n3. Squirtle")

    First_Pokemon = input ("Choose Your First Pokemon: ")
    if First_Pokemon in "1":
        Main_Bulbasaur.choose()
    elif First_Pokemon in "2":
        Main_Charmander.choose()
    elif First_Pokemon in "3":
        Main_Squirtle.choose()
    else :
        print("Wrong input\n")
        first_choose()


# #load save game
# def starting():
#     action = input("You want to open saved game or start new game[save/new]: ")
#     action = action.lower()
#     if action ==  "save":
#         with open("data.txt", "r") as f:
#             a = f.read()
#             pass
            
#     elif action == "new":
#         first_choose()
#     else:
#         print("Wrong input\n")
#         starting()

# starting()

first_choose()