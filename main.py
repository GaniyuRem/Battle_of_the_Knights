from Player import Player
from Knight import Knight
from DrawKnight import Draw
import time, os
from DrawKnight import Draw
from Art import Art


screen=Draw()
one=Player()
two=Player()
aciis_art=Art()
game_over="Game play cancelled"

try:
    while (one.get_knight.get_kinght_hlth_score() != 0 and  two.get_knight.get_kinght_hlth_score() !=0 and one.get_knight.get_kinght_hlth_score() > 0 and  two.get_knight.get_kinght_hlth_score() >  0) :
        os.system("date")
        print("\n ==|>====> Now battling <====<|== \n")
        one.get_knight.set_chosen_random_state()
        two.get_knight.set_chosen_random_state()
        one.get_knight.set_knight_action_state(one.get_knight.get_chosen_random_state())
        two.get_knight.set_knight_action_state(two.get_knight.get_chosen_random_state())
        one.get_knight.set_ascii_art(aciis_art.player_one[one.get_knight.get_knight_action_state()])
        two.get_knight.set_ascii_art(aciis_art.player_two[two.get_knight.get_knight_action_state()])
        screen.kinght_action_move_details(one.get_knight,two.get_knight)
        screen.check_winner(one.get_knight,two.get_knight)

        print(screen.join_art(one.get_knight.get_ascii_art(),two.get_knight.get_ascii_art()))
        print(f"{one.get_player_name()}  The {one.get_knight.get_knight_name()} : {one.get_knight.get_kinght_hlth_score()} ==>--<== {one.get_knight.get_knight_action_state()} ==>--<== ")
        print(f"{two.get_player_name()}  The {two.get_knight.get_knight_name()} : {two.get_knight.get_kinght_hlth_score()} ==>--<== {two.get_knight.get_knight_action_state()} ==>--<== \n")
        time.sleep(0.5)
except KeyboardInterrupt:
    print(game_over)



