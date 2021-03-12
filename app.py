#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, redirect, url_for, render_template, session, jsonify
# Use `render_template` to send user to a different page; Redirect 301
# Use `request` to GET or POST from HTML form.
# Use `session` to pass server-side information/request

import requests, os

# Initialize the app by creating an Environment instance, and registering your assets with it in the form of so called bundles.
from flask_assets import Environment, Bundle

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

bundles = {

    'all_js': Bundle(
        'js/jquery.min.js',
        'bootstrap/js/bootstrap.bundle.min.js',
        'js/scripts.js',
        output='gen/all.js'),

    'all_css': Bundle(
        'bootstrap/css/bootstrap.min.css',
        'fontawesome/css/all.css',
        'css/style.css',
        output='gen/all.css'),
}
assets = Environment(app)
assets.register(bundles)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route("/")
@app.route("/index/")
# Define the website pages
def home():
    return render_template('pages/index.html')


@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)