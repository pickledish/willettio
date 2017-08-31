#----------------------------------------------------------------------------#
# Importing libraries that we use, plus all blueprints
#----------------------------------------------------------------------------#

import urllib, os, sys
from flask import Flask, url_for
from flask_script import Manager
import logging; from logging import Formatter, FileHandler

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/Colors")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/MainSite")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/MonteCarlo")

from WillettApp import willettApp
from ColorApp import colorApp
from MonteCarlo import monteCarloApp

#----------------------------------------------------------------------------#
# Registering all the blueprints on their specified URL zones
#----------------------------------------------------------------------------#

app = Flask(__name__, static_url_path = "/irrelevantStatic")
app.register_blueprint(willettApp, url_prefix='')
app.register_blueprint(colorApp, url_prefix='/colors')
app.register_blueprint(monteCarloApp, url_prefix="/monteCarlo")

manager = Manager(app)

#----------------------------------------------------------------------------#
# Stolen from stackoverflow! List all URL routes for this app
#----------------------------------------------------------------------------#

@manager.command
def list_routes():

	output = []
	for rule in app.url_map.iter_rules():

		options = {}
		for arg in rule.arguments: options[arg] = "[{0}]".format(arg)

		methods = ','.join(rule.methods)
		url = url_for(rule.endpoint, **options)
		s = "{:50s} {:20s} {}"
		line = urllib.parse.unquote(s.format(rule.endpoint, methods, url))
		output.append(line)

	for line in sorted(output): print(line)

#----------------------------------------------------------------------------#
# Assuming we're in production, set up the logging tools
#----------------------------------------------------------------------------#

if not app.debug:

    file_handler = FileHandler('error.log')
    s = "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
    file_handler.setFormatter(Formatter(s))

    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == "__main__":
	manager.run()



