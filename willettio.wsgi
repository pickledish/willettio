#!/usr/bin/python3

import sys
from werkzeug.wsgi import DispatcherMiddleware

sys.path.insert(1, '/var/www/willettio')
sys.path.insert(2, '/var/www')

from mainPage import app as frontend
application = DispatcherMiddleware(frontend, {})
