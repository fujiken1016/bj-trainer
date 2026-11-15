# Wizard of Odds basic strategy charts, transcribed 2026-11-16 (J542)
# https://wizardofodds.com/games/blackjack/strategy/1-deck/ (bj_1d_s17.gif, bj_1d_h17.gif)
# https://wizardofodds.com/games/blackjack/strategy/2-decks/ (bj_2d_s17.gif, bj_2d_h17.gif)
# https://wizardofodds.com/games/blackjack/strategy/4-decks/ (bj_4d_s17.gif, bj_4d_h17.gif)  4-8 decks
# https://wizardofodds.com/games/blackjack/strategy/european/ (bj_euro.gif) 6D S17 DAS dbl9-11 no-peek
# columns: dealer 2..10, A.  D = "Dh"
def r(s): 
  v=s.split(); assert len(v)==10,(s,len(v)); return v
H10=r("H H H H H H H H H H"); S10=r("S S S S S S S S S S"); P10=r("P P P P P P P P P P")
T={}
T["1S"]={"hard":{**{t:H10 for t in range(4,8)},8:r("H H H D D H H H H H"),9:r("D D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D D"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H H H"),16:r("S S S S S H H H Rh Rh"),**{t:S10 for t in range(17,22)}},
 "soft":{13:r("H H D D D H H H H H"),14:r("H H D D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("D D D D D H H H H H"),
  18:r("S Ds Ds Ds Ds S S H H S"),19:r("S S S S Ds S S S S S"),20:S10,21:S10},
 "pair":{2:r("Ph P P P P P H H H H"),3:r("Ph Ph P P P P Ph H H H"),4:r("H H Ph Pd Pd H H H H H"),6:r("P P P P P Ph H H H H"),7:r("P P P P P P Ph H Rs H"),8:P10,9:r("P P P P P S P P S S"),11:P10}}
T["1H"]={"hard":{**{t:H10 for t in range(4,8)},8:r("H H H D D H H H H H"),9:r("D D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D D"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H H Rh"),16:r("S S S S S H H H Rh Rh"),17:r("S S S S S S S S S Rs"),**{t:S10 for t in range(18,22)}},
 "soft":{13:r("H H D D D H H H H H"),14:r("H H D D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("D D D D D H H H H H"),
  18:r("S Ds Ds Ds Ds S S H H H"),19:r("S S S S Ds S S S S S"),20:S10,21:S10},
 "pair":{2:r("Ph P P P P P H H H H"),3:r("Ph Ph P P P P Ph H H H"),4:r("H H Ph Pd Pd H H H H H"),6:r("P P P P P Ph H H H H"),7:r("P P P P P P Ph H Rs Rh"),8:P10,9:r("P P P P P S P P S Ps"),11:P10}}
T["2S"]={"hard":{**{t:H10 for t in range(4,9)},9:r("D D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D D"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H Rh H"),16:r("S S S S S H H H Rh Rh"),**{t:S10 for t in range(17,22)}},
 "soft":{13:r("H H H D D H H H H H"),14:r("H H H D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("H D D D D H H H H H"),
  18:r("S Ds Ds Ds Ds S S H H H"),19:S10,20:S10,21:S10},
 "pair":{2:r("Ph Ph P P P P H H H H"),3:r("Ph Ph P P P P H H H H"),4:r("H H H Ph Ph H H H H H"),6:r("P P P P P Ph H H H H"),7:r("P P P P P P Ph H H H"),8:P10,9:r("P P P P P S P P S S"),11:P10}}
T["2H"]={"hard":{**{t:H10 for t in range(4,9)},9:r("D D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D D"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H Rh Rh"),16:r("S S S S S H H H Rh Rh"),17:r("S S S S S S S S S Rs"),**{t:S10 for t in range(18,22)}},
 "soft":{13:r("H H H D D H H H H H"),14:r("H H D D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("H D D D D H H H H H"),
  18:r("Ds Ds Ds Ds Ds S S H H H"),19:r("S S S S Ds S S S S S"),20:S10,21:S10},
 "pair":{2:r("Ph Ph P P P P H H H H"),3:r("Ph Ph P P P P H H H H"),4:r("H H H Ph Ph H H H H H"),6:r("P P P P P Ph H H H H"),7:r("P P P P P P Ph H H H"),8:r("P P P P P P P P P Rp2"),9:r("P P P P P S P P S S"),11:P10}}
T["6S"]={"hard":{**{t:H10 for t in range(4,9)},9:r("H D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D H"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H Rh H"),16:r("S S S S S H H Rh Rh Rh"),**{t:S10 for t in range(17,22)}},
 "soft":{13:r("H H H D D H H H H H"),14:r("H H H D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("H D D D D H H H H H"),
  18:r("S Ds Ds Ds Ds S S H H H"),19:S10,20:S10,21:S10},
 "pair":{2:r("Ph Ph P P P P H H H H"),3:r("Ph Ph P P P P H H H H"),4:r("H H H Ph Ph H H H H H"),6:r("Ph P P P P H H H H H"),7:r("P P P P P P H H H H"),8:P10,9:r("P P P P P S P P S S"),11:P10}}
T["6H"]={"hard":{**{t:H10 for t in range(4,9)},9:r("H D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D D D"),
  12:r("H H S S S H H H H H"),13:r("S S S S S H H H H H"),14:r("S S S S S H H H H H"),15:r("S S S S S H H H Rh Rh"),16:r("S S S S S H H Rh Rh Rh"),17:r("S S S S S S S S S Rs"),**{t:S10 for t in range(18,22)}},
 "soft":{13:r("H H H D D H H H H H"),14:r("H H H D D H H H H H"),15:r("H H D D D H H H H H"),16:r("H H D D D H H H H H"),17:r("H D D D D H H H H H"),
  18:r("Ds Ds Ds Ds Ds S S H H H"),19:r("S S S S Ds S S S S S"),20:S10,21:S10},
 "pair":{2:r("Ph Ph P P P P H H H H"),3:r("Ph Ph P P P P H H H H"),4:r("H H H Ph Ph H H H H H"),6:r("Ph P P P P H H H H H"),7:r("P P P P P P H H H H"),8:r("P P P P P P P P P Rp"),9:r("P P P P P S P P S S"),11:P10}}
T["EURO"]={"hard":{**{t:H10 for t in range(4,9)},9:r("H D D D D H H H H H"),10:r("D D D D D D D D H H"),11:r("D D D D D D D D H H"),
  12:r("H H S S S H H H H H"),**{t:r("S S S S S H H H H H") for t in range(13,17)},**{t:S10 for t in range(17,22)}},
 "soft":{**{t:H10 for t in range(13,18)},18:r("S S S S S S S H H H"),19:S10,20:S10,21:S10},
 "pair":{2:r("P P P P P P H H H H"),3:r("P P P P P P H H H H"),4:r("H H H P P H H H H H"),5:r("D D D D D D D D H H"),6:r("P P P P P H H H H H"),7:r("P P P P P P H H H H"),8:r("P P P P P P P P H H"),9:r("P P P P P S P P S S"),10:S10,11:r("P P P P P P P P P H")}}
