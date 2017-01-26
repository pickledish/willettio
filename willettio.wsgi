#!/usr/bin/python3

import sys
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

#sys.path.insert(0, '/Users/brandon/Dropbox/Personal')
#sys.path.insert(1, '/Users/brandon/Dropbox/Personal/willettio')
#sys.path.insert(2, '/Users/brandon/Dropbox/Personal/willettio/linearApp')
sys.path.insert(0, '/var/www')
sys.path.insert(1, '/var/www/willettio')
sys.path.insert(2, '/var/www/willettio/linearApp')

from mainPage import app as frontend
from linearApp import app as linear
application = DispatcherMiddleware(frontend, {"/linear": linear})

if __name__ == "__main__": run_simple('localhost', 8080, application, use_reloader=True)
