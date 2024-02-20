from Art import Art

class Draw:
	def __init__(self) -> None:
		self.__aciis_art = Art()

	def join_art(self,player_one,player_two,str_between='        '):
		lines1 = player_one.split('\n')
		lines2 = player_two.split('\n')
		max_dist = max([len(s) for s in lines1])
		f_str = '{:<'+str(max_dist)+'}{}{}'
		players = "\n".join([f_str.format(knight_one,str_between,knight_two) for knight_one,knight_two in zip(lines1,lines2)])
		return players

	def kinght_action_move_details(self,player_one,player_two)->"obj":
		player_one_action_state=player_one.get_knight_action_state()
		player_two_action_state=player_two.get_knight_action_state()

		if player_one_action_state == "defend" and player_two_action_state == "defend":
			player_one.knight_hlth_defence_damage()
			player_two.knight_hlth_defence_damage()

		if player_one_action_state == "rest" and player_two_action_state == "rest":
			player_one.knight_hlth_rest_damage()
			player_two.knight_hlth_rest_damage()

		if player_one_action_state == "attack" and  player_two_action_state == "defend":
			player_two.knight_hlth_defence_damage()


		if player_one_action_state == "attack" and  player_two_action_state == "rest":
			player_two.knight_hlth_rest_damage()


		if player_one_action_state == "defend" and  player_two_action_state == "rest":
			player_two.knight_hlth_rest_damage()
			player_one.knight_hlth_defence_damage()

		# player2

		if player_two_action_state == "attack" and player_one_action_state == "attack":
			player_one.knight_hlth_attack_damage()
			player_two.knight_hlth_attack_damage()			

		if player_two_action_state == "attack" and player_one_action_state == "defend":
			player_one.knight_hlth_defence_damage()


		if player_two_action_state == "attack" and player_one_action_state == "rest":
			player_one.knight_hlth_rest_damage()

		if player_two_action_state == "defend" and player_one_action_state == "rest":
			player_one.knight_hlth_rest_damage()
	
	def check_winner(self,player_one,player_two):
		if (player_one.get_kinght_hlth_score() <= 0 and player_two.get_kinght_hlth_score() >= 0) or (player_one.get_kinght_hlth_score() < 0 and player_two.get_kinght_hlth_score() > 0):
			player_one.set_knight_action_state("defeat")
			player_one.set_ascii_art(self.__aciis_art.player_one[player_one.get_knight_action_state()]) 

		if (player_two.get_kinght_hlth_score() <= 0 and player_one.get_kinght_hlth_score() >= 0)  or (player_two.get_kinght_hlth_score() < 0 and player_one.get_kinght_hlth_score() > 0):
			player_two.set_knight_action_state("defeat")
			player_two.set_ascii_art(self.__aciis_art.player_two[player_two.get_knight_action_state()])
 
		if (player_one.get_kinght_hlth_score() >= 1 and player_two.get_kinght_hlth_score() <= 0) or (player_one.get_kinght_hlth_score() > 0 and player_two.get_kinght_hlth_score() < 0):
			player_one.set_knight_action_state("winner")
			player_one.set_ascii_art(self.__aciis_art.player_one[player_one.get_knight_action_state()])

		if (player_two.get_kinght_hlth_score() >= 1 and player_one.get_kinght_hlth_score() <= 0) or (player_two.get_kinght_hlth_score() > 0 and player_one.get_kinght_hlth_score() < 0):
			player_two.set_knight_action_state("winner")
			player_two.set_ascii_art(self.aciis_art.player_two[player_two.get_knight_action_state()])

		

