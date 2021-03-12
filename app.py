#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, redirect, url_for, render_template, session, jsonify
# Use `render_template` to send user to a different page; Redirect 301
# Use `request` to GET or POST from HTML form.
# Use `session` to pass server-side information/request

import requests, json, os

# Initialize the app by creating an Environment instance, and registering your assets with it in the form of so called bundles.
from flask_assets import Environment, Bundle

# Creating HTML Forms — Flask-WTF
from flask_wtf import FlaskForm
from wtforms import SelectField

#----------------------------------------------------------------------------#
# MTA Data Feeds
#----------------------------------------------------------------------------#

# The root directory requires a .env file with API_KEY assigned/defined within
# and dotenv installed from pypi. Get API key from http://datamine.mta.info/user
api_key = os.environ['API_KEY']


#----------------------------------------------------------------------------#
# Check Feed Once
#----------------------------------------------------------------------------#

# MTA NYC Transit Station Locations – Updated February 17, 2021
station_location = 'Stations.csv'
station_location_csv = pd.read_csv(station_location, header=0)
subway_stations = list(station_location_data.values)
station_resp = requests.head(station_location)

# Elevator and Escalator Equipment - API Key
def getEquipData():
    elevescequip = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene_equipments.json', headers={"x-api-key": api_key, "Content-Type":"application/json"})
    # print('elevescequip',elevescequip)
    return elevescequip

#----------------------------------------------------------------------------#
# Check Feed every 5 minutes
#----------------------------------------------------------------------------#
# Elevator and Escalator Outage - API Key
def getOutageStatus():
    elevesc_outage = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json', headers={"x-api-key": api_key, "Content-Type":"application/json"})
    # print('elevesc_outage',elevesc_outage)
    return elevesc_outage
    
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

# Define the secret key which is a way to decrypt and encrypt
app.config.from_pyfile('config.py')
# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')

# Define the secret key which is a way to decrypt and encrypt
app.secret_key = os.environ.get('SECRET_KEY')
 
#----------------------------------------------------------------------------#
# Functions
#----------------------------------------------------------------------------#

# Create NYC boroughs list
borough_dict = {}
def nyc_boros():
    boroughs = None
    if elevescequip.status_code == 200:
        elevescequip_boros = json.loads(elevescequip.text)
        boroughs = set(x['borough'] for x in elevescequip_boros)

        for b in boroughs:
            if b == 'BX':
                borough_dict[b] = "The Bronx"
            elif b == 'QNS':
                borough_dict[b] = "Queens"
            elif b == 'BKN':
                borough_dict[b] = "Brooklyn"
            elif b == 'MN':
                borough_dict[b] = "Manhattan"
            else:
                borough_dict["Other"] = "Other"
    else:
        print('Error', elevescequip.status_code)
 
# Render HTML Form with borough and filter drop downs
class EquipFilterForm(FlaskForm):
    nyc_boros()

    boro_station = SelectField('boroughs', choices=[('selected', 'Select a boroughs...')]+[(k,v) for k,v in borough_dict.items()], render_kw={"class": "form-select"})
    equip_filter_type = SelectField('equip_type', choices=[('all', 'All'),('elev','Elevator'),('esc', 'Escalator'),('outages', 'Outages')], render_kw={"class": "form-select"})


#----------------------------------------------------------------------------#
# Steps
#   Check the status code for 200 (found)
#   Parse equipment and station data to match station id
#   latlong
#----------------------------------------------------------------------------#
def createStationFeed(equipData, stationData):
    # function parse and merge data
    pass

class StationMapping():
    def __init__(self, feed):
        self.feed = feed
        
    def allstations(self):
        # grabbing the feed
        pass
    
    def elevstations(self):
        # return only elevators
        pass

    def escstations(self):
        # return only escalators
        pass
    
    def outagestations(self):
        pass

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route("/")
@app.route("/index/")
# Define the website pages
def home():
    equip_map = EquipFilterForm()
    return render_template('pages/index.html', form=equip_map)


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