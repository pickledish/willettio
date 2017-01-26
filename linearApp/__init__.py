from calculations import *
import numpy as np
import time, pdb, os

from flask import Flask
from flask import render_template, request
app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/linear"

@app.route('/', methods=['POST', 'GET'])
def index():

	if (request.method == 'POST'):

		if (request.form['n'] != '-1'):

			print(request.form['alpha'])
			
			size = int(request.form['n'])
			alpha = float(request.form['alpha'])
			beta = float(request.form['beta'])
			gamma = float(request.form['gamma'])
			enteredA = str(request.form['matrixA'])
			enteredb = str(request.form['matrixb'])

			print (enteredA)
			print (enteredb)
			print("----------------------")

			numpyA = np.zeros((size, size))
			temp_list = enteredA.split("\n")
			symmetry = False
			for i in range(len(temp_list)):
				line = temp_list[i]
				np_row = np.fromstring(line, dtype=float, sep=',')

				if (np_row.size == 0): 
					np_row = np.zeros((1, size))
				elif (np_row.size < size):
					symmetry = True
					while (np_row.size < size): np_row = np.append(np_row, [0], axis = 0) 
				numpyA[i,:] = np_row

			if (symmetry):
				for i in range(size):
					numpyA[i,:] = numpyA[:,i]

			numpyb = np.zeros((size, 1))
			temp_list = enteredb.split("\n")
			for i in range(len(temp_list)):
				line = temp_list[i]
				np_row = np.fromstring(line, dtype=float, sep=',')
				if (np_row.size == 0): np_row = np.zeros((1, 1))
				numpyb[i,:] = np_row

			print (numpyA, "\n", numpyb)
			global origin

			try: 
				origin, algorithmState, randomState, algorithmMean, randomMean = main(size, alpha, beta, gamma, numpyA, numpyb)

				return render_template('output.html', Before = list(zip(origin.A, origin.X, origin.B)),
													  bestState = algorithmState,
													  time = str(int(time.time())),
													  randomState = randomState, algoMean = algorithmMean, randMean = randomMean)

			except Exception as e:
				return "An error occurred in the processing of the algorithm:\n" + str(e) + "\nPlease refresh the page to try again


		else:
			return "Please enter valid numbers"

	else:
		return render_template('systems.html')

@app.route('/matrix/')
def matrixRoute():
	return render_template("infoMini.html", Before = list(zip(origin.A, origin.X, origin.B)))

@app.route('/rerun/', methods = ['GET', 'POST'])
def rerun():

	if (request.form['keep'] != 'no'):

		global origin
		
		keepRows = request.form['keep']

		pdb.set_trace()

		rowList = [int(i) for i in keepRows.split(",")]
		size = len(rowList)
		smallState = origin.createSubstateFromList(rowList)

		origin, algorithmState, randomState, algorithmMean, randomMean = main(size, 0, 0, 0, smallState.A, smallState.B)

		return render_template('output.html', Before = list(zip(origin.A, origin.X, origin.B)),
												  bestState = algorithmState,
												  time = str(int(time.time())),
												  randomState = randomState, algoMean = algorithmMean, randMean = randomMean)


	else:
		return "Please enter valid numbers"




