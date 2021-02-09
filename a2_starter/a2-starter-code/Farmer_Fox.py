'''Farmer_Fox.py
by Haokun Cai
UWNetID: haokun
Student number: 1832787

Assignment 2, in CSE 415, Winter 2021.

This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.


#<METADATA>
PROBLEM_NAME = "Framer_Fox"
PROBLEM_VERSION="1.0"
PROBLEM_AUTHORS = ['H. Cai']
PROBLEM_CREATION_DATE = "20-JAN-2021"
#</METADATA>

# <COMMON DATA>
# 0 for state at left side of river
# 1 for state at right side of river
LEFT = 0
RIGHT = 1
# all passenger are in an array
FA = 0  # framer
F = 1  # fox
C = 2  # chicken
G = 3  # grain
# </COMMON DATA>

# <COMMON CODE>
class State():

    def __init__(self, d):
        if d is None:
            d = {'passengers': [[0, 0], [0, 0], [0, 0], [0, 0]],
                 'boat': LEFT}
        self.d = d

    def __eq__(self, s2):
        for prop in ['passengers', 'boat']:
            if self.d[prop] != s2.d[prop]:
                return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        p = self.d['passengers']
        txt = "\n Farmer on left:"+str(p[FA][LEFT])+"\n"
        txt += " Fox on left:"+str(p[F][LEFT])+"\n"
        txt += " Chicken on left:"+str(p[C][LEFT])+"\n"
        txt += " Grain on left:"+str(p[G][LEFT])+"\n"
        txt += "   Farmer on right:"+str(p[FA][RIGHT])+"\n"
        txt += "   Fox on right:"+str(p[F][RIGHT])+"\n"
        txt += "   Chicken on right:"+str(p[C][RIGHT])+"\n"
        txt += "   Grain on right:"+str(p[G][RIGHT])+"\n"
        side = 'left'
        if self.d['boat'] is 1:
            side = 'right'
        txt += " boat is on the "+side+".\n"
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.d['passengers'] = [self.d['passengers'][Ffcg][:] for Ffcg in [FA, F, C, G]]
        news.d['boat'] = self.d['boat']
        return news

    def can_move(self, fa, f, c, g):
        side = self.d['boat']
        p = self.d['passengers']
        if fa < 1:  # framer must be on the same side
            return False
        # check availability on fox, chicken, grain
        fox_available = p[F][side]
        chicken_available = p[C][side]
        grain_available = p[G][side]
        if fox_available < f:
            return False
        if chicken_available < c:
            return False
        if grain_available < g:
            return False

        # condition for each possible rider combinations
        fox_remaining = fox_available - f
        chicken_remaining = chicken_available - c
        grain_remaining = grain_available - g

        if fox_remaining == 1 and chicken_remaining == 1:
            return False
        elif chicken_remaining == 1 and grain_remaining == 1:
            return False

        return True

    def move(self, fa, f, c, g):
        news = self.copy()
        side = self.d['boat']
        p = news.d['passengers']
        p[FA][side] = p[FA][side] - fa     # Remove people from the current side.
        p[F][side] = p[F][side] - f
        p[C][side] = p[C][side] - c
        p[G][side] = p[G][side] - g

        p[FA][1-side] = p[FA][1-side] + fa  # Add them at the other side.
        p[F][1-side] = p[F][1-side] + f
        p[C][1-side] = p[C][1-side] + c
        p[G][1-side] = p[G][1-side] + g

        news.d['boat'] = 1-side       # Move the boat itself.

        return news


def goal_test(s):
    # all the riders are on the right side
    p = s.d['passengers']
    return p[FA][RIGHT] and p[F][RIGHT] and p[G][RIGHT] and p[C][RIGHT]


def goal_message(s):
    return "You have made it! Farmer and Chicken and Fox and Grain cross" \
               "the river and unharm! "


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)
# </COMMON CODE>


# <INITIAL_STATE>


CREATE_INITIAL_STATE = lambda: State(d={'passengers': [[1, 0], [1, 0], [1, 0], [1, 0]],
                                        'boat': LEFT})


# </INITIAL_STATE>

# <OPERATORS>


Ffcg_combinations = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1)]

OPERATORS = [Operator(
  "Cross the river with "+str(fa)+" farmers, "+str(f)+" fox, "+str(c)+" chicken, and "+str(g)+" grain",
  lambda s, fa=fa, f=f, c=c, g=g: s.can_move(fa, f, c, g),
  lambda s, fa=fa, f=f, c=c, g=g: s.move(fa, f, c, g) )
  for (fa, f, c, g) in Ffcg_combinations]


# </OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>
