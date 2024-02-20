class Art:

 def __init__(self):
  self.player_one={
   "attack":"""\
     O     /\n\
  ---+--- /\n\
    / \\ \n\
   /   \\ \n\
 """,
    "defend":"""\
    O    | \n\
 ---+--- | \n\
   / \\   | \n\
  /   \\  | \n\
""",
 "rest":"""\
    O \n\
 ---+---\n\
   / \\ \n\
  /   \\ \n\
""",
"defeat":"""\
      \n\
  o -- + -- \ \n\
             \ \n\
""",
"winner":"""\
  \ O / \n\
    +  \n\
   / \\ \n\
  /   \\ \n\
"""
  }
  self.player_two={"attack":"""\
   \     O   \n\
    \ ---+--- \n\
        / \\ \n\
       /   \\ \n\
  """,
    "defend":"""\
  |    O  \n\
  | ---+---\n\
  |   / \\ \n\
  |  /   \\ \n\
 """,
 "rest":"""\
    O  \n\
 ---+---\n\
   / \\ \n\
  /   \\ \n\
""",
"defeat":"""\
      \n\
  / -- + -- o\n\
 /    \n\
""",
"winner":"""\
  \ O / \n\
    +  \n\
   / \\ \n\
  /   \\ \n\
"""
  }

def get_player_one_aciis_art_states(self):
 return self.player_one

  # EXTRA FUNCTIONS: TYPE OF WEAPON WITH BIGGER DAMAGES
