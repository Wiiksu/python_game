from typing import Tuple, Union

# Player-----

class Character:
  def __init__(self, name:str):
    self.id = id(self)
    self.name = name
    self.attack = int(10)
    self.health = int(100)
    self.inventory = []
    self.coords = [5, 5]
    self.alive = True
  
  def __str__(self) -> str:
    print(f"\nname: {self.name} health: {self.health} attack: {self.attack}")
    
  def get_health(self) -> int:
    return self.health
  
  def set_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.alive = False
      
  def get_inventory(self):
    return self.inventory
  
  def set_inventory(self, item: str):
    self.inventory.append(item.lower())
  
  def set_x_coord(self, direction):
    if direction == "e" and self.coords[0] < 5:
      if self.coords == [2,3]:
        print("\nI come across an impenetrable wall made out of obsidian. I should look for a door..")
      elif self.coords == [3,3]:
        print("\nThe only exit is through north..")
      else:
        self.coords[0] = self.coords[0] + 1
        print(f"\n{self.name} moves east")
    elif direction == "w" and self.coords[0] > 1:
      if self.coords == [4,3]:
        print("\nI come across an impenetrable wall made out of obsidian. I should look for a door..")
      elif self.coords == [3,3]:
        print("\nThe only exit is through north..")
      else:
        self.coords[0] = self.coords[0] - 1
        print(f"\n{self.name} moves west")
    else:
        print("\nI'm blocked by a wall..")
  
  def set_y_coord(self, direction):
    if direction == "s" and self.coords[1] < 5:
      if self.coords == [3,2] and "old key" not in self.inventory:
        print("\nMy path is blocked by an old door with a rusty lock and runic symbols.. I should look for a key")
      elif self.coords == [3,2] and "old key" in self.inventory:
        self.coords[1] = self.coords[1] + 1
        print("\nI insert the old key inside the lock and it opens with a satisfying click. I step into the darkness")
      elif self.coords == [3,3]:
        print("\nThe only exit is through north..")
      else:
        self.coords[1] = self.coords[1] + 1
        print(f"\n{self.name} moves south")
    elif direction == "n" and self.coords[1] > 1:
      if self.coords == [3,4]:
        print("\nI come across an impenetrable wall made out of obsidian. I should look for a door..")
      else:
        self.coords[1] = self.coords[1] - 1
        print(f"\n{self.name} moves north")
    else:
        print("\nI'm blocked by a wall..")
      
  def check_items(self):
    if len(self.inventory) < 1:
      print("\nI rummage around my bag and find nothing..")
      return False
    else:
      print(f"\nMy inventory contains: {self.inventory}")
      return True
    
  def use_item(self, player_input):
    player_input_lower = player_input.lower()
    if player_input_lower in self.inventory:
      print(f"\nI decide to use {player_input_lower}")
      if player_input_lower == "potion":
        print("\nI feel invigorated!")
        self.inventory.remove(player_input_lower)
        if self.health <= 80:
          self.health += 20
        else:
          self.health == 100
      elif player_input_lower == "the sword of vanquishing":
        print("\nThe power of the sword flows through me!")
        self.inventory.remove(player_input_lower)
        self.attack += 15
      elif player_input_lower == "the crown of domination" and self.coords != [5, 5]:
        print("\nI put on the crown and prepare myself..")
        self.inventory.remove(player_input_lower)
        return "bad_end"
      elif player_input_lower == "the crown of domination" and self.coords == [5, 5]:
        print("\nI put on the crown and prepare myself..")
        self.inventory.remove(player_input_lower)
        return "good_end"
      elif player_input_lower == "old key":
        print("\nI have a feeling this key is somehow important..")
        return "key"
    else:
      print("\nI have no such item in my inventory")
      return "invalid_input"
    
      
# Enemies-----

class Goblin(Character):
  def __init__(self):
    self.id = id(self)
    self.name = "Goblin"
    self.attack = int(3)
    self.health = int(20)
    self.alive = True
    
  def set_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.alive = False
      
class Orc(Character):
  def __init__(self):
    self.id = id(self)
    self.name = "Orc"
    self.attack = int(5)
    self.health = int(40)
    self.alive = True
    
  def set_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.alive = False
      
class Boss(Character):
  def __init__(self):
    self.id = id(self)
    self.name = "The Dungeon Master"
    self.attack = int(20)
    self.health = int(125)
    self.alive = True
    
  def set_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.alive = False
      
# Rooms-----

class Room:
  def __init__(self, loot: Union[str, None], enemy: Union[Goblin, Orc, Boss, None], description: str, visual: str = "   ", coords: Tuple[int, int] = (0, 0)):
    self.id = id(self)
    self.loot = loot
    self.enemy = enemy
    self.description = description
    self.visual = "   " if loot is None else visual
    self.coords = coords
    
  def has_enemy(self, player_coords):
    if self.enemy is not None and tuple(player_coords) == self.coords:
      return self.enemy
    else:
      return False