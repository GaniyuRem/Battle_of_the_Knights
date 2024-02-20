class Player:
  from Knight import Knight
  from NameGeneration import NameGenerator

  def __init__(self) -> None:
    self.__player_name=self.NameGenerator().player_name_generation()
    self.__knight= self.Knight()
  
  def get_player_name(self):
    return self.__player_name

  @property
  def get_knight(self):
    return self.__knight