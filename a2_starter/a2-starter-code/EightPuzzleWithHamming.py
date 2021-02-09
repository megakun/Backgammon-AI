''''EightPuzzleWithHamming.py
	This file contains a Eightpuzzle with heuristic implemetation
	'So it can be use by an A star implementation
	The particular heuristic is hamming distance
	ie, the number of plate out of place

'''
from EightPuzzle import *

def h(self):
	Hamming = 0
	num = 0

	for i in range(0, 3):
		for j in range(0, 3):
			if self.b[i][j] != num:
				Hamming += 1
			num += 1
	return Hamming - 1