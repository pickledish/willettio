import numpy as np
from math import sqrt
import random, pdb

class State:

	rowNum = 0
	includedRows = []

	def __init__(self, A, B, r = list()):

		self.A = A
		self.B = B

		self.rowNum = len(B)
		self.includedRows =  list(range(0, self.rowNum)) if (not r) else r

		self.X = np.linalg.solve(A, B)
		self.normalized = self.getNormalized()
		self.theta = self.getTheta()

	def __gt__(self, other):
		return self.theta > other.theta

	def __eq__(self, other):
		return self.theta == other.theta

	def getTheta(self):

		numerator = (self.normalized * self.B).sum()

		denominator = 0.0
		for i in range(self.rowNum):
			for j in range(self.rowNum):
				if (i == j): denominator += (self.normalized[i]**2) * (self.A[i,i]**2)
				else: denominator += self.normalized[i] * self.normalized[j] * self.A[i,j]

		return (numerator / sqrt(denominator))

	def getNormalized(self):
		sumX = self.X.sum()
		return np.array([ (x / sumX) for x in self.X])


	# When given just an integer, it picks (that integer) random rows/cols to include in the result
	def createSubstate(self, newSize):

		selectedRows = random.sample(self.includedRows, newSize)
		rowsToInclude = [self.includedRows.index(elem) for elem in selectedRows]

		try:
			smallerA = self.A[:, rowsToInclude]
			smallerA = smallerA[rowsToInclude, :]
			smallerB = self.B[rowsToInclude, :]
		except:
			pdb.set_trace()

		return State(smallerA, smallerB, rowsToInclude)

	# When given a list, it keeps the specific rows and columns mentioned in that list in the result
	def createSubstateFromList(self, rowsToInclude):

		smallerA = self.A[:, rowsToInclude]
		smallerA = smallerA[rowsToInclude, :]
		smallerB = self.B[rowsToInclude, :]

		return State(smallerA, smallerB, rowsToInclude)





