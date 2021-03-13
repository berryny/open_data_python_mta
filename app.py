#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, redirect, url_for, render_template, session, jsonify
# Use `render_template` to send user to a different page; Redirect 301
# Use `request` to GET or POST from HTML form.
# Use `session` to pass server-side information/request

import requests, json, os

import pandas as pd
import numpy as np

# Initialize the app by creating an Environment instance, and registering your assets with it in the form of so called bundles.
from flask_assets import Environment, Bundle

# Creating HTML Forms — Flask-WTF
from flask_wtf import FlaskForm
from wtforms import SelectField

#----------------------------------------------------------------------------#
# Use API key to access MTA Data
#----------------------------------------------------------------------------#
from dotenv import load_dotenv, find_dotenv # imports module for dotenv
load_dotenv(find_dotenv()) # loads .env from root directory

# The root directory requires a .env file with API_KEY assigned/defined within
# and dotenv installed from pypi. Get API key from http://datamine.mta.info/user
api_key = os.environ['API_KEY']


#----------------------------------------------------------------------------#
# Check Feed Once
#----------------------------------------------------------------------------#

# MTA NYC Transit Station Locations – Updated February 17, 2021
# station_location = 'https://atisdata.s3.amazonaws.com/Station/Stations.csv'
station_location = './dataset/Stations.csv'

def parseStations():
    station_location_data = pd.read_csv(station_location, header=0)
    df = pd.DataFrame(station_location_data)
    mapStationArr = []

    if (df.size <= 0):
        raise Exception("CSV Not Found")
    else:    
        adaelevesc = getEquipData()
        for i in df.index:

            for selected_station in adaelevesc:
                if df.loc[i, 'Complex ID'] == int(selected_station['stationcomplexid']):
                    mapStationObj = {}
                    mapStationObj['Station'] = selected_station
                    mapStationObj['Coordinates'] = [df.loc[i, 'GTFS Latitude'], df.loc[i, 'GTFS Longitude']]
                    mapStationArr.append(mapStationObj)
        
        # print('mapStationArr',mapStationArr)
        return mapStationArr

# Elevator and Escalator Equipment - API Key
def getEquipData():
    elevescequip = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene_equipments.json', headers={"x-api-key": api_key, "Content-Type":"application/json"})
    # print('elevescequip',elevescequip)
    if elevescequip.status_code == 200:
        return json.loads(elevescequip.text)
    else:
        raise Exception("Equipment data not found")

#----------------------------------------------------------------------------#
# Data ref every 5 minutes
#----------------------------------------------------------------------------#
# Elevator and Escalator Outage - API Key
def getOutageStatus():
    elevesc_outage = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json', headers={"x-api-key": api_key, "Content-Type":"application/json"})
    print('elevesc_outage',elevesc_outage)
    if (elevesc_outage):
        return elevesc_outage
    else:
        raise Exception("Outage status not found")
# getOutageStatus()

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

bundles = {

    'all_js': Bundle(
        'js/jquery.min.js',
        'bootstrap/js/bootstrap.bundle.min.js',
        'leaflet/leaflet.js',
        'js/scripts.js',
        output='gen/all.js'),

    'all_css': Bundle(
        'bootstrap/css/bootstrap.min.css',
        'fontawesome/css/all.css',
        'leaflet/leaflet.css',
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

def nyc_boros():
    elevescequip_boros = getEquipData()
    boroughs = set(x['borough'] for x in elevescequip_boros)
    borough_dict = {}
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
   
    return borough_dict

 
# Render HTML Form with borough and filter drop downs
class EquipFilterForm(FlaskForm):
    borough_dict = nyc_boros()
    boro_station = SelectField('boroughs', choices=[('selected', 'Select a boroughs...')]+[(k,v) for k,v in borough_dict.items()], render_kw={"class": "form-select"})
    equip_filter_type = SelectField('equip_type', choices=[('elevator','Elevator'),('escalator', 'Escalator'),('powerwalk', 'Power Walk')], render_kw={"class": "form-select"})
    # ('all', 'All'),('outages', 'Outages')

def parseEquipmentType():
    # function parse and merge data
    parsestations = parseStations()
    statELArr = []
    statESArr = []
    statPWArr = []

    for _station in parsestations:
        if _station['Station']['equipmenttype'] == 'EL':
            statELArr.append(_station)
        elif _station['Station']['equipmenttype'] == 'ES':
            statESArr.append(_station)
        elif _station['Station']['equipmenttype'] == 'PW':
            statPWArr.append(_station)
        else:
            print('else',  _station['Station']['equipmenttype'])

    equipmentTypes = {'elevator': statELArr, 'escalator': statESArr, 'powerwalk': statPWArr}
    return equipmentTypes
    
class StationMapping:
    def __init__(self, borough, equipment):
        self.boro = borough
        self.equip = equipment
        self.parsed_data = parseEquipmentType()
        # print('station',self)
        
    def allstations(self):
        # return all stations
        print("outagestations", self)
        return None

    def elevstations(self):
        # return stations with elevators
        stationDict = self.parsed_data
        return self.filterMap(stationDict['elevator'])

    def escstations(self):
        # return stations with escalators
        stationDict = self.parsed_data
        return self.filterMap(stationDict['escalator'])
    
    def pwstations(self):
        # return stations with power walk
        stationDict = self.parsed_data
        return self.filterMap(stationDict['powerwalk'])
    
    def filterMap(self,typeofEquip):
        filterArr = []
        for flt in typeofEquip:
            if flt['Station']['borough'] == self.boro:
                filterArr.append(flt)
        if filterArr:
            return filterArr
        else:
            return None

    def outagestations(self):
        # return only equip outages
        print("outagestations", self)
        return None

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

@app.route("/stations_with_equip/<borough_filter>/<equip_filter>/", methods=['GET', 'POST'])
def stations_with_equip(borough_filter,equip_filter):
    
    print("borough_filter",borough_filter)
    print("equip_filter",equip_filter)
    stations = StationMapping(borough_filter,equip_filter)
    getCoordinates = ''

    if equip_filter == 'all':
       stations.allstations()
    elif equip_filter == 'elevator':
        print('elevator')
        getCoordinates = stations.elevstations()
    elif equip_filter == 'escalator':
        print('escalator')
        getCoordinates = stations.escstations()
    elif equip_filter == 'powerwalk':
        getCoordinates = stations.pwstations()
            
    elif equip_filter == 'outages':
        print('outages')
        getCoordinates = stations.outagestations()
    else:
        print('else')
        getCoordinates = stations.allstations()

    return jsonify({'status': getCoordinates})

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)
