import math, pdb, os
import numpy as np
from numpy.linalg import LinAlgError
from scipy.stats import norm
import random
from StateModule import State

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
plt.style.use('ggplot')

# Generate random numbers for arrays A and b, and then solve the system and return them all
def MakeOriginalState(size, alpha, beta, gamma, RF):
	array_A = np.zeros((size, size))

	# Generating the A array from appropriate values
	it = np.nditer(array_A, flags=['multi_index'], op_flags=['readwrite'])
	while not it.finished:
		random.seed()
		if (it.multi_index[0] == it.multi_index[1]):
			it[0] = random.uniform(0, beta)
		else:
			it[0] = random.uniform((gamma*(-1)), gamma)
		it.iternext()

	# Generating the b array with appropriate values from alpha
	array_b = np.zeros((size, 1))

	for elem in np.nditer(array_b, op_flags=['readwrite']):
		random.seed()
		elem[...] = random.uniform(0, alpha) - RF

	return State(array_A, array_b)

def plotHelper(variety, **kwargs):

	plt.clf()
	print(os.getcwd())
	print("PRITNED THE WORKING DIRECTORY")
	os.chdir('linearApp')

	if (variety == "single"):

		thetas = len(thetaList)

		for i in range(0, thetas):
			plt.plot(i+1, thetaList[i], 'ro')

		axes = plt.gca()
		axes.set_xlim([0, thetas+1])
		plt.ylabel("Theta")
		plt.xlabel("Iteration Number", labelpad=12)
		plt.title("Theta over Multiple Iterations", y=1.04)
		plt.savefig("static/graph.png")

	elif (variety == "histogram"):

		s = kwargs['size']
		c = kwargs['counted']
		i = kwargs['removed']

		argsorted_counted = sorted(range(len(c)), key = lambda a: c[a], reverse = True)

		fig, ax = plt.subplots(1)

		textstr = "These row numbers sorted from highest-influence to lowest-influence are:\n" + str(argsorted_counted)
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		ax.text(0.00, -0.20, textstr, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)

		plt.bar(list(range(s)), c, color = "#600090")
		plt.ylabel("Occurances of X_i", labelpad=12)
		plt.xlabel("Particular X_i", labelpad=12)
		plt.title("Histogram of X_i with Greatest Effect on Theta", y=1.04)
		plt.savefig("static/graph_of_" + str(i) + "_rowscols.png", bbox_inches = "tight", pad_inches = 0.67)

	elif (variety == "phiCompare"):

		perfectList = kwargs['stateList']

		for state in perfectList:
			plt.scatter(state.rowNum, state.theta, c = "#600090")
		
		axes = plt.gca()
		axes.set_xlim([0, len(perfectList) + 1])
		plt.ylabel("Best Found Phi")
		plt.xlabel("Number of Rows Deleted", labelpad=12)
		plt.title("Best Phi from Removing i Rows", y=1.04)
		plt.savefig("static/phiCompare.png")

	elif (variety == "verify"):

		randomStates = kwargs['states']
		best = kwargs['best']

		minThetaState = min(randomStates)
		maxThetaState = max(randomStates)

		rtNumpy = np.array([state.theta for state in randomStates])
		mean = rtNumpy.mean()
		deviation = rtNumpy.std()
		normObject = norm(loc = mean, scale = deviation)

		rang = np.linspace(int(mean - 4*deviation), int(mean + 4*deviation), 1000)

		plt.plot(rang, normObject.pdf(rang), 'k')

		plt.axvline(x= best, ymin=0.0, ymax = 1.0, linewidth=1, color = "#600090")

		axes = plt.gca()
		plt.ylabel("Frequency of Value of Theta")
		plt.xlabel("Value of Theta", labelpad=12)
		plt.title("Verification Test", y=1.04)
		plt.savefig("static/verify.png")

	os.chdir('..')

def determineBestRows(stateList, size):

	baseline = origin
	occurances = list([origin])

	for currentState in stateList:

		delta = currentState.theta - baseline.theta
		if (delta < 0):

			uRef = random.uniform(0, 1)
			p = math.exp(delta / origin.theta)

			if (p > uRef): baseline = currentState
			else: pass

		else: baseline = currentState

		occurances.append(baseline)

	counted = list([0] * size)
	for state in occurances:
		for row in state.includedRows:
			counted[row] += 1

	return counted

def main(size, alpha, beta, gamma, enteredMatrixA, enteredMatrixb):

	# ------------------------ Set up the original state ------------------------

	NumIterations = 1000
	global origin

	try:
		print (str(enteredMatrixA.shape) + " and " + str(enteredMatrixb.shape))
		origin = State(enteredMatrixA, enteredMatrixb)

	except LinAlgError:
		RF = 0.05
		origin = MakeOriginalState(size, alpha, beta, gamma, RF)

	# -------------------- Perform tests on each possible nRow -------------------

	perfectList = list()
	for i in range(1, size):

		stateList = list()
		for j in range(NumIterations):
			smallerState = origin.createSubstate(i)
			stateList.append(smallerState)

		occurances = determineBestRows(stateList, size)

		plotHelper("histogram", size = size, counted = occurances, removed = i)

		argSort = sorted(range(len(occurances)), key = occurances.__getitem__, reverse = True)
		bestRows = argSort[:i]

		bestGivenSize = origin.createSubstateFromList(bestRows)
		perfectList.append(bestGivenSize)

	plotHelper("phiCompare", stateList = perfectList)

	# -------------------- Compare to randomly-generated states ---------------------

	randomStates = list()
	for i in range(3000):

		nRow = random.randint(1, size-1)
		rando = origin.createSubstate(nRow)
		randomStates.append(rando)

	bestAlgorithmState = max(perfectList)
	bestRandomState = max(randomStates)

	plotHelper("verify", states = randomStates, best = bestAlgorithmState.theta)

	# ---------------- If random created a better state, test resiliency -----------------

	if (bestRandomState.theta > (bestAlgorithmState.theta + 0.01)):

		reslience_random, reslience_algorithm = list(), list()
		for i in range(100):

			t = bestRandomState.createSubstate(bestRandomState.rowNum - 1)
			reslience_random.append(t)

			t = bestAlgorithmState.createSubstate(bestAlgorithmState.rowNum - 1)
			reslience_algorithm.append(t)

		randomMean = np.mean([i.theta for i in reslience_random])
		algorithmMean = np.mean([i.theta for i in reslience_algorithm])

	else:
		randomMean, algorithmMean = 0, 0

	return [origin, bestAlgorithmState, bestRandomState, algorithmMean, randomMean]













