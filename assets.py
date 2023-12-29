welcome_screen = r"""
                           ___
                          ( ((
                           ) ))           -THE DANKEST DUNGEON-
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))       Created by Wiiksu a.k.a Henri S. 
                          (_((     
                                      
  """

thanks = r"""
 _______ _                 _           __                   _             _             _ 
|__   __| |               | |         / _|                 | |           (_)           | |
   | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ | | __ _ _   _ _ _ __   __ _| |
   | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | |
   | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |_) | | (_| | |_| | | | | | (_| |_|
   |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, (_)
                                                     | |             __/ |         __/ |  
                                                     |_|            |___/         |___/        
                                                                                               
"""

bad = r"""
 ____          _____    ______ _   _ _____  _ 
|  _ \   /\   |  __ \  |  ____| \ | |  __ \| |
| |_) | /  \  | |  | | | |__  |  \| | |  | | |
|  _ < / /\ \ | |  | | |  __| | . ` | |  | | |
| |_) / ____ \| |__| | | |____| |\  | |__| |_|
|____/_/    \_\_____/  |______|_| \_|_____/(_)

Your soul has been twisted and will dominated by the dark crown.. You will serve an eternity as the new Dungeon Master!

"""

good = r"""
  _____  ____   ____  _____    ______ _   _ _____  _ 
 / ____|/ __ \ / __ \|  __ \  |  ____| \ | |  __ \| |
| |  __| |  | | |  | | |  | | | |__  |  \| | |  | | |
| | |_ | |  | | |  | | |  | | |  __| | . ` | |  | | |
| |__| | |__| | |__| | |__| | | |____| |\  | |__| |_|
 \_____|\____/ \____/|_____/  |______|_| \_|_____/(_)

The crown has been purified and the dungeons curse lifted! The walls crumble around you and you walk happily towards the sunrise!

"""

over = r"""
  _____          __  __ ______    ______      ________ _____  _ 
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \| |
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /| |
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \|_|
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_(_)    
                                                   
"""

intro_text = r"""
"I wake up, my head throbbing with a dull ache. The air is damp and heavy.. My surroundings are barely visible in the dim light, and the only sounds are the distant drips of water and the eerie whispers of unseen creatures. My memory seems fragmented, and I struggle to recall how I ended up here.. Shadows dance along the walls, and the occasional growls and snarls pierce the air. I must navigate this labyrinthine dungeon and confront the challenges that lie ahead. The journey begins, and I can't shake the feeling that my fate is entwined with the secrets hidden within these walls."

"""

scroll = r"""
  ______________________________________________
=(__    ___      __     _     ____     ___   ___)=
   |                                           |
   |                                           |
   |   'To vanquish the Master,                |
   |    a blade of power you must wield,'      |
   |                                           |
   |   'Find the Sword of Vanquishing          |
   |     on the ancient battlefield,'          |
   |                                           |
   |   'Seek the Crown of Domination,          |
   |     a regal treasure rare,'               |
   |                                           |
   |   'In the room with the pillar of light,  |
   |     its destiny to wear.'                 |
   |                                           |
   |                                           |
  _|    ___      __     _     ____     ___   __|
=(______________________________________________)=

"""

descriptions = [
    "\na cold room with frozen stone walls and two thick wooden doors leading south and east. Judging by the armored skeletons all around an ancient battle was fought here. ",  # coords: (1.1)
    "\na cold room with frozen stone walls and three thick wooden doors leading east, west and south.",  # coords: (2.1)
    "\na cold room with frozen stone walls and three thick wooden doors leading east, west and south. you sense something unsettling from the south.",  # coords: (3.1)
    "\na cold room with frozen stone walls and three thick wooden doors leading east, west and south.",  # coords: (4.1)
    "\na cold room with frozen stone walls and two thick wooden doors leading south and west.",  # coords: (5.1)
    "\na slightly cold room with stone walls cold to the touch and three thick wooden doors leading north, south and east.",  # coords: (1.2)
    "\na slightly cold room with stone walls cold to the touch and four thick wooden doors leading to all directions.",  # coords: (2.2)
    "\na slightly cold room with stone walls cold to the touch and three thick wooden doors leading east, west and north and one strange door to the south. you feel something omnious from the south.",  # coords: (3.2)
    "\na slightly cold room with stone walls cold to the touch and four thick wooden doors leading to all directions.",  # coords: (4.2)
    "\na slightly cold room with stone walls cold to the touch and three thick wooden doors leading north, south and west.",  # coords: (5.2)
    "\na room with foreboding atmosphere, dark walls and three thick wooden doors leading north, south and east. you sense something unsettling from the east.",  # coords: (1.3)
    "\na room with foreboding atmosphere, dark walls and three thick wooden doors leading north, south and west. you feel something omnious from the east.",  # coords: (2.3)
    "\nThe walls and doors of this room are ever moving and distorting, a tattered red carpet leads to the back of the room where you spot a massive throne. You are completely surrounded by darkness and malice.",  # coords: (3.3)
    "\na room with foreboding atmosphere, dark walls and three thick wooden doors leading south, north and east. you feel something omnious from the west.",  # coords: (4.3)
    "\na room with foreboding atmosphere with stone walls and three thick wooden doors leading north, south and west. you sense something unsettling from the west.",  # coords: (5.3)
    "\na slightly warm room with stone walls and three thick wooden doors leading north, south and east.",  # coords: (1.4)
    "\na slightly warm room with stone walls and four thick wooden doors leading to all directions.",  # coords: (2.4)
    "\na slightly warm room with stone walls and three thick wooden doors leading east, west and south. you feel something omnious from the north.",  # coords: (3.4)
    "\na slightly warm room with stone walls and four thick wooden doors leading to all directions.",  # coords: (4.4)
    "\na slightly warm room with stone walls and three thick wooden doors leading north, south and west.",  # coords: (5.4)
    "\na warm room with marble walls and two thick wooden doors leading north and east.",  # coords: (1.5)
    "\na warm room with marble walls and three thick wooden doors leading east, west and north.",  # coords: (2.5)
    "\na warm room marble walls and three thick wooden doors leading east, west and north. you sense something unsettling from the north.",  # coords: (3.5)
    "\na warm room with marble walls and three thick wooden doors leading east, west and north.",  # coords: (4.5)
    "\na warm room with marble walls and two thick wooden doors leading north and west. a round opening in the ceiling projects a pillar of light in the center of the room.",  # coords: (5.5)
]

sword_in_inventory = '\nDungeon Master: "Ah, a mighty sword in your inventory! Are you saving it for a tea party, adventurer? Wield your assets!"'

no_sword_in_inventory = '\nDungeon Master: "Empty-handed? Did you plan to tickle me into submission? Your preparation is as sharp as a butter knife, my brave hero."'

sword_is_equipped = '\nDungeon Master: "Well, well! A sword in hand. I didnt expect that. Now youve got my attention, adventurer. Lets hope you know how to use it."'

wrong_input = "[Invalid input, type 'help' to list the game controls.]"

fight_help = """
----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                |
| type 'y' to fight an enemy if there is currently an alive one in the same room. Type 'n' to exit the battle-menu and escape.   |
|                                                                                                                                |
----------------------------------------------------------------------------------------------------------------------------------
"""

controls = """
-----------------------------------------------------------------------------------------------------------------
|                                                                                                               |
| ['back' to navigate back from sub-menus such as 'move' and 'bag']                                             |
|                                                                                                               |
| ['status' to print out your stats]                                                                            |
|                                                                                                               |
| ['move' to open the movement-menu.]                                                                           |
|                                                                                                               |
| ['look' to look around observe your environment and to find loot.]                                            |
|                                                                                                               |
| ['bag' to open up the inventory-menu and print out your current inventory.]                                   |
|                                                                                                               |
| ['map' to open up your map and visually confirm your location.]                                               |
|                                                                                                               |
| ['fight' to initiate battle-mode. You dont have to fight the enemies you encounter and may sneak past them.]  |
|                                                                                                               |
| ['exit' to close the game. Only works in main-menu.]                                                          |
|                                                                                                               |
| ['help' to bring up the game-controls.]                                                                       |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------
"""

move_help = """
----------------------------------------------------------
|                                                        |
| ['n', 'e', 's', 'w'] to move inside the movement menu. |
|                                                        |
| 'back' to exit the movement-menu.                      |
|                                                        |
----------------------------------------------------------
"""

inventory_help = """
-----------------------------------------------------------------------------------------
|                                                                                       |
| to use an item in your inventory-menu type the name of the item inside the inventory, |
| for example type 'potion' to use a potion if your inventory contains such an item.    |
|                                                                                       |
| 'back' to exit the inventory-menu.                                                    |
|                                                                                       |
-----------------------------------------------------------------------------------------
"""
