#!/usr/bin/python3

import sys
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

sys.path.insert(0, '/Users/brandon/Desktop/test')
sys.path.insert(1, '/Users/brandon/Desktop/test/willettio')
sys.path.insert(2, '/Users/brandon/Desktop/test/willettio/linearApp')

from mainPage import app as frontend
from linearApp import app as linear
application = DispatcherMiddleware(frontend, {"/linear": linear})

if __name__ == "__main__": run_simple('localhost', 8080, application, use_reloader=True)
