class Knight:
  import random
  from NameGeneration import NameGenerator

  knight_states=['attack','defend','rest']

  def __init__(self):
    self.__knight_hlth_score=100
    self.__knight_hlth_attack_hit=Knight.random.randrange(1,15)
    self.__knight_hlth_attack_rest=0
    self.__knight_hlth_attack_defence=0
    self.__knight_name=self.NameGenerator().knight_name_generation()
    self.__knight_action_state=""
    self.__knight_ascii_art="" 
    self.__chosen_random_state=''

  def set_knight_name(self,knight_name):
    self.__knight_name=knight_name

  
  def set_knight_action_state(self,knight_states):
    self.__knight_action_state=knight_states
  
  def knight_hlth_attack_damage(self)-> int:
    self.__knight_hlth_score -=  self.__knight_hlth_attack_hit
  
  def knight_hlth_rest_damage(self)-> int:
    self.__knight_hlth_score -= self.__knight_hlth_attack_rest
  
  def knight_hlth_defence_damage(self):
    self.__knight_hlth_score -= self.__knight_hlth_attack_defence  
 
  def get_kinght_hlth_score(self) -> int:
    return self.__knight_hlth_score 
  
  def get_knight_action_state(self)-> str:
    return self.__knight_action_state

  def get_knight_name(self)->str:
    return self.__knight_name
  
  def set_ascii_art(self,knight_ascii_value) -> "NONE":
    self.__knight_ascii_art=knight_ascii_value

  def get_ascii_art(self):
    return self.__knight_ascii_art
  
  def set_chosen_random_state(self):
    self.__chosen_random_state=Knight.random.choice(Knight.knight_states)
  
  def get_chosen_random_state(self):
    return self.__chosen_random_state

