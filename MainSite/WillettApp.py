#----------------------------------------------------------------------------#
# Imports and blueprint setup
#----------------------------------------------------------------------------#

from flask import Flask, Blueprint, render_template, request

willettApp = Blueprint('willettApp', __name__, 
	template_folder = 'templates', static_folder = 'static')

#----------------------------------------------------------------------------#
# Basic views -- Displaying choice screen or results, with data
#----------------------------------------------------------------------------#

@willettApp.route('/')
def home():
    return render_template('index.html')


@willettApp.route('/about')
def about():
    return render_template('aboutMe.html')

#----------------------------------------------------------------------------#
# Error handling! For when you screw up or I screw up
#----------------------------------------------------------------------------#

@willettApp.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@willettApp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


