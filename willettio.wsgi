#!/usr/bin/python3
from werkzeug.wsgi import DispatcherMiddleware
import sys

sys.path.insert(0, "/usr/lib/python3.4")
sys.path.insert(1, '/var/www/willettio')
sys.path.insert(2, '/var/www')

from mainPage import app as frontend
application = DispatcherMiddleware(frontend)
