import random


class NameGenerator:
  
 def __init__(self) -> None:
    pass
 def knight_name_generation(self):
   knight = ["Brave","Horrific","Courageous","Terrific","Fair","Conqueror","Victorious","Glorious","Invicible"]
   knight =  random.choice(knight)
   return knight
  
  
 def player_name_generation(self):
   generate_player_name = ["Ganiyu","Charles","Henry","William","James","Richard","Edward"]
   generate_player_name = random.choice(generate_player_name)
   return generate_player_name 
  
