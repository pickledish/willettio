#!/usr/bin/python3

import sys
from werkzeug.wsgi import DispatcherMiddleware

sys.path.insert(0, '/var/www')
sys.path.insert(1, '/var/www/willettio')
sys.path.insert(2, '/var/www/willettio/linearApp')

from mainPage import app as frontend
from linearApp import app as linear
application = DispatcherMiddleware(frontend, {
	'/linear': linear
})
