import time
from classes import Room, Goblin, Orc, Boss, Character
from assets import descriptions, welcome_screen, thanks, over, wrong_input, controls, move_help, inventory_help, fight_help, intro_text, good, bad, scroll, sword_in_inventory, sword_is_equipped, no_sword_in_inventory

# Game ascii-screens-----

def welcome():
  for char in welcome_screen:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
def intro():
  for char in intro_text:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
def thank_you():
  for char in thanks:
        print(char, end='', flush=True)
        time.sleep(0.001)
        
def game_over():
  for char in over:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
def good_end():
  for char in good:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
def bad_end():
  for char in bad:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
def open_scroll():
  for char in scroll:
      print(char, end='', flush=True)
      time.sleep(0.001)
      
# Create enemy and room objects to dungeon list and return-----

def create_dungeon():
  dungeon = []
  skull = u" \u2620 "
  Orc1 = Orc()
  Orc2 = Orc()
  Orc3 = Orc()
  Goblin1 = Goblin()
  Goblin2 = Goblin()
  Goblin3 = Goblin()
  Goblin4 = Goblin()
  Goblin5 = Goblin()
  Goblin6 = Goblin()
  Dungeon_Master = Boss()
  
  r1 = Room("The Sword of Vanquishing", Orc3, descriptions[0], coords=(1,1))
  r2 = Room(None, None, descriptions[1], coords=(2,1))
  r3 = Room(None, None, descriptions[2], coords=(3,1))
  r4 = Room("Dung", Goblin5, descriptions[3], coords=(4,1))
  r5 = Room(None, None, descriptions[4], coords=(5,1))
  r6 = Room(None, None, descriptions[5], coords=(1,2))
  r7 = Room("Scroll Part 3", Goblin4, descriptions[6], coords=(2,2))
  r8 = Room(None, None, descriptions[7], coords=(3,2))
  r9 = Room(None, None, descriptions[8], coords=(4,2))
  r10 = Room("Old Key", Goblin6, descriptions[9], coords=(5,2))
  r11 = Room(None, None, descriptions[10], coords=(1,3))
  r12 = Room(None, None, descriptions[11], coords=(2,3))
  r13 = Room("The Crown of Domination", Dungeon_Master, descriptions[12], visual=skull, coords=(3,3))
  r14 = Room(None, None, descriptions[13], coords=(4,3))
  r15 = Room("Potion", Orc2, descriptions[14], coords=(5,3))
  r16 = Room("Dung", Goblin3, descriptions[15], coords=(1,4))
  r17 = Room(None, None, descriptions[16], coords=(2,4))
  r18 = Room("Scroll Part 2", Goblin2, descriptions[17], coords=(3,4))
  r19 = Room(None, None, descriptions[18], coords=(4,4))
  r20 = Room(None, None, descriptions[19], coords=(5,4))
  r21 = Room("Potion", Orc1, descriptions[20], coords=(1,5))
  r22 = Room(None, None, descriptions[21], coords=(2,5))
  r23 = Room("Scroll Part 1", Goblin1, descriptions[22], coords=(3,5))
  r24 = Room(None, None, descriptions[23], coords=(4,5))
  r25 = Room(None, None, descriptions[24], coords=(5,5))
  
  dungeon.extend([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25])
  
  return dungeon

# Print map-graphics-----

def open_map(room, player_coords):
  chess = u" \u265F "
  grid = [
        room[:5],
        room[5:10],
        room[10:15],
        room[15:20],
        room[20:],
    ]

  map_str = "\n--------------------------\n"
  for i, row in enumerate(grid):
      map_str += "|"
      for j, room in enumerate(row):
          if [j + 1, i + 1] == player_coords:
              map_str += f"{chess} |"
          else:
              map_str += f"{room.visual} |"
      map_str += "\n--------------------------\n"
      
  print(map_str)
  
# helper for look_around() function to make enemy names grammatically correct
  
def get_enemy_placeholder(enemy_name):
    if enemy_name == "the goblin":
        return "a pathetic goblin! HAH!"
    elif enemy_name == "the orc":
        return "an orc! He smells awful!"
    elif enemy_name == "the dungeon master":
      return "a tall, dark, and ominous figure clad in heavy plate armor, with a spiky crown adorning his head. His glowing red eyes are staring directly at me. Yikes!"
    else:
        return enemy_name

# helper for look_around() function to make item names grammatically correct
  
def get_item_placeholder(item_name):
    if item_name == "Potion":
      return "a potion, this could be handy."
    elif item_name == "Scroll Part 1" or item_name == "Scroll Part 2" or item_name == "Scroll Part 3":
      return "a ripped piece of what seems to be an ancient scroll, I should collect all the parts."
    elif item_name == "The Sword of Vanquishing":
      return "a sword that stands out from all the other rusted weapons inside the room. The blade glows with a faint light and the pommel has carved runes on it. Cool! Maybe I should use this?"
    elif item_name == "The Crown of Domination":
      return "the crown that fell from the dark lords head as I bested him. The crown seems to suck all light around it except the glow from my sword. The runes on the crown look inverted, maybe it's a clue?"
    elif item_name == "Old Key":
      return "an old key, this seems important."
    elif item_name == "Dung":
      return "goblin-shit? ewwww.."
    else:
        return item_name
      
# keeps track of the scroll parts in players inventory
          
def check_scroll(player_inventory):
  if "scroll part 1" in player_inventory and "scroll part 2" in player_inventory and "scroll part 3" in player_inventory:
    print("\nFinally I have all the parts! I piece them all together and place the newly formed scroll inside my bag.")
    parts_to_remove = ["scroll part 1", "scroll part 2", "scroll part 3"]
    for part in parts_to_remove:
      if part in player_inventory:
          player_inventory.remove(part)
    player_inventory.append("ancient scroll")
      
# Check for loot in room-objects and add to player-object inventory-----
  
def look_around(dungeon, player_coords, player_inventory, player_attack):
  for room in dungeon:
    if room.coords == tuple(player_coords):
        print(room.description)
        if room.has_enemy(player_coords) and room.enemy.alive:
          enemy_placeholder = get_enemy_placeholder(room.enemy.name)
          print(f"\nI am not alone. I peer into the shadows and spot {enemy_placeholder}")
          if room.enemy.name == "the dungeon master" and player_attack == 25:
            print(sword_is_equipped)
          elif room.enemy.name == "the dungeon master" and "the sword of vanquishing" in player_inventory:
            print(sword_in_inventory)
          elif room.enemy.name == "the dungeon master" and "the sword of vanquishing" not in player_inventory:
            print(no_sword_in_inventory)
        elif room.loot != None and room.enemy == None:
          loot_placeholder_empty = get_item_placeholder(room.loot)
          print(f"\nSomething in the room catches my attention. I pick up {loot_placeholder_empty}.")
          player_inventory.append(room.loot.lower())
          check_scroll(player_inventory)
          room.loot = None
        elif room.loot != None and room.enemy.alive == False:
          loot_placeholder_enemy = get_item_placeholder(room.loot)
          print(f"\nNow that the room is clear of the threat I look around and pick up {loot_placeholder_enemy}.")
          player_inventory.append(room.loot.lower())
          check_scroll(player_inventory)
          room.loot = None
          
# Check room objects for enemy objects for fight-function-----
          
def check_for_enemy(dungeon, player_coords, player_char):
    for room in dungeon:
      if room.coords == tuple(player_coords):
        if room.has_enemy(player_coords) and room.enemy.alive:
          print(f"\nBattle-mode initiated against {room.enemy.name}!")
          player_input = input(f"\n[Battle-menu]: Should I fight against {room.enemy.name}? (y/n) ").lower()
          if player_input == "y":
            result = player_fight(player_char, room.enemy)
            if result == True:
              return True
          elif player_input == "n" or player_input == "back":
            print(f"\nI sneak past {room.enemy.name} leaving all possible loot behind. Am I really this scared?")
          elif player_input == "help":
            print(fight_help)
          else:
            print(wrong_input)
        elif room.has_enemy(player_coords) and room.enemy.alive == False:
          print(f"\n{room.enemy.name.capitalize()} is definitely dead. No use in defiling a corpse?")
        else:
          print(f"\n{player_char.name} starts shadow-boxing as there are no opponents in the room. Not a bad workout!")
          
# Player and Enemy object fight-logic, returns boolean depending on outcome-----

def player_fight(player_char, enemy):
  print("\nCombat has started! I put on my war-face and charge the enemy!")
  while player_char.alive and enemy.alive:
    time.sleep(0.5)
    print(f"{player_char.name} attacks! Take that!!")
    enemy.set_health(player_char.attack)
    time.sleep(0.5)
    print(f"{player_char.name} dealt {player_char.attack} damage to {enemy.name}! {enemy.name.capitalize()} has {enemy.health} health left!")
    if enemy.alive == False:
      print(f"{enemy.name.capitalize()} dies!")
      time.sleep(0.5)
      print(f"{player_char.name} wins! is it time for a victory-dance?")
      break
    time.sleep(0.5)
    print(f"{enemy.name} attacks! OUCH!")
    player_char.set_health(enemy.attack)
    time.sleep(0.5)
    print(f"{enemy.name} dealt {enemy.attack} damage to {player_char.name}! {player_char.name} has {player_char.health} health left!")
    if player_char.alive == False:
      time.sleep(0.5)
      print(f"{player_char.name} dies! NOOO!!")
      return True
    
# Calls player-objects coordinate-move-methods to set player.coords. Uses room.has_enemy method to look for enemies in movement-menu-----
    
def player_move(player_char, dungeon):
  print(move_help)
  while True:
    movement = input("\n[Movement-menu]: Where should I move? ")
    if movement == "back":
      break
    elif movement == "w" or movement == "e":
      player_char.set_x_coord(movement)
      for room in dungeon:
        if room.coords == tuple(player_char.coords):
          if room.has_enemy(player_char.coords) and room.enemy.alive:
            print("\nI spot something moving in the shadows. Spooky!")
    elif movement == "n" or movement == "s":
      player_char.set_y_coord(movement)
      for room in dungeon:
        if room.coords == tuple(player_char.coords):
          if room.has_enemy(player_char.coords) and room.enemy.alive:
            print("\nI spot something moving in the shadows. Spooky!")
    elif movement == "help":
      print(move_help)
    else:
      print(wrong_input)
      
# If check_items player-method returns true asks to use items from player-objects inventory-----
      
def player_inventory(player_char):
  print(inventory_help)
  print("\nI take a look inside my bag")
  while player_char.check_items():
      player_input = input("\n[Inventory-menu]: Should I use an item? (y/n) ").lower()
      if player_input == "help":
        print(inventory_help)
      elif player_input == "n" or player_input == "back":
        break
      elif player_input == "y":
        inventory_use = input("\n[Use-menu]: Which item should I use? ").lower()
        if inventory_use == "help":
          print(inventory_help)
        elif inventory_use == "back":
          break
        else:
          result = player_char.use_item(inventory_use)
          if result == "bad_end":
            return "bad_end"
          if result == "good_end":
            return "good_end"
          if result == "open_scroll":
            open_scroll()
            break
      else:
        print("\nInvalid input")
            
def create_char():
  intro()
  while True:
    player_input = input("\nWhat is my name? ")
    if len(player_input) > 20:
      print("\nI don't remember my name being this long. I need to think harder.")
    else:
      player = Character(str(player_input.lower().capitalize()))
      print(f"\nYes.. That's right.. my name is {player_input.lower().capitalize()}!")
      return player
    
# Creates player and dungeon objects to player_menu function if the user wants to play-----

def game_start():
  exit_flag = False
  welcome()
  while not exit_flag:
    game_start = input("\nStart your adventure? (y/n) ").lower()
    if game_start == "y":
      player = create_char()
      dungeon = create_dungeon()
      player_menu(player, dungeon)
      exit_flag = True
    elif game_start == "n":
      exit_flag = True
    else:
      print("\nInvalid input")
      
# Main-menu to navigate to the sub-menus, checks for triggers to game over flags depending on returns from player_inventory() and check_for_enemy()-----

def player_menu(player_char, dungeon):
  print(f"\nWelcome to the Dankest Dungeon adventurer! If you're stuck type 'help' to bring out the game-controls.")
  game_over_flag = False
  while not game_over_flag:
    player_input = input("\n[Main-menu]: What should I do? ").lower()
    if player_input == "exit":
      thank_you()
      break
    elif player_input == "help":
      print(controls)
    elif player_input == "status":
      player_char.__str__()
    elif player_input == "move":
      player_move(player_char, dungeon)
    elif player_input == "look":
      look_around(dungeon, player_char.coords, player_char.inventory, player_char.attack)
    elif player_input == "map":
      open_map(dungeon, player_char.coords)
    elif player_input == "bag":
      result = player_inventory(player_char)
      if result == "bad_end":
        bad_end()
        game_over_flag = True
      elif result == "good_end":
        good_end()
        game_over_flag = True
    elif player_input == "fight":
      result = check_for_enemy(dungeon, player_char.coords, player_char)
      if result == True:
        game_over()
        game_over_flag = True
    else:
      print(wrong_input)