''''EightPuzzleWithMahttern.py
	This file contains a Eightpuzzle with heuristic implemetation
	'So it can be use by an A star implementation
	The particular heuristic is manhattern distance
	ie, the number of plate out of place

'''
import math
from EightPuzzle import *

def h(self):
	Manhattern = 0
	num = 0
	
	for i in range(0, 3):
		for j in range(0, 3):
			curr = self.b[i][j]
			if (curr != 0):
				(vi, vj) = (curr // 3, curr % 3)
				(ti, tj) = (num // 3, num % 3)
				Manhattern += abs(vi - ti) + abs(vj - tj)
			num += 1		
	return Manhattern

