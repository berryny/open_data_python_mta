# Welcome to Python Flask Boilerplate

## What is Python?

![](https://raw.githubusercontent.com/berryny/hourofcode_python/main/python-logo.gif)

[Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.

[source](https://en.wikipedia.org/wiki/Python_%28programming_language%29)

## Python HTML Template

Jinja [Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures) "is a modern and designer-friendly templating language for Python, modelled after Django's templates."

## What is Flask?

Flask is a microframework for Python based on Werkzeug and Jinja2.

## Third-party Libraries

- [Bootstrap](https://getbootstrap.com/) "is a free and open-source CSS framework directed at responsive, mobile-first front-end web development."
- [Font Awesome](https://fontawesome.com/) "is a font and icon toolkit based on CSS and Less."
- [Leaflet](https://leafletjs.com/download.html) "an open-source JavaScript library for mobile-friendly interactive maps"
  - [Mapbox Streets](https://www.mapbox.com/maps/streets) is a comprehensive, general-purpose map that emphasizes accurate, legible styling of road and transit networks.

# Environment Setup Installation

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/downloads)

# Get MTA API

- Get API key from https://api.mta.info/#/signup

# Software Installation

- [Anaconda](https://www.anaconda.com/) is the birthplace of Python data science.
- [Visual Studio Code](https://code.visualstudio.com/) is a code editor redefined and optimized for building and debugging modern web and cloud applications.
    - Python extension for Visual Studio Code [install](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 
    - [Try Jupyter](https://jupyter.org/try)
    - [Jupyter notebooks with Binder](https://mybinder.org/)

## Layout Ideas

Helpful UX/UI tools to layout out your thoughts before design.

- [Behance](https://www.behance.net/search/projects?field=ui%2Fux) Design ideas
- [Figma](https://www.figma.com/)
- [Adobe XD](https://www.adobe.com/products/xd.html)

## Quick Start

- Clone the repo:
  ```
  git clone https://github.com/berryny/open_data_python_mta.git
  cd open_data_python_mta
  ```
  - Or place into a custom name folder
  ```
  git clone https://github.com/berryny/open_data_python_mta.git custom-name-folder
  cd custom-name-folder
  ```
- Install Virtual Environment:
```
pip install virtualenv
virtualenv venv
```
```
py -m venv venv/
```
  - For Mac users
  ```
  source venv/bin/activate
  ```
  - For Windows users
  ```
  venv\Scripts\activate.bat
  ```
  - For Powershell
  ```
  venv\Scripts\activate.ps1
  ```
-  Install the dependencies:
  ```
  pip install -r requirements.txt
  ```
- Create a `.env` file in the root directory
  - Add to file
  ```
  SECRET_KEY=CREATEYOUROWNSECRETKEY
  API_KEY=MTAAPIKEYGOESHERE
  ```

-  Run the development server:
  ```
  py app.py
  ```
-  Run the production server:
  ```
  flask run
  ```
- Navigate to 
    - [http://localhost:5000](http://localhost:5000)
    - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - To stop server Press CTRL+C to quit 

## Folder Tree

```
|   .env
|   .gitignore
|   .slugignore
|   app.py
|   config.py
|   favicon.ico
|   Procfile
|   Procfile.windows
|   README.md
|   requirements.txt
|   
+---dataset
|       Stations.csv
|       
+---static
|   +---bootstrap
|   |   +---css
|   |   |       bootstrap-grid.css
|   |   |       bootstrap-grid.css.map
|   |   |       bootstrap-grid.min.css
|   |   |       bootstrap-grid.min.css.map
|   |   |       bootstrap-grid.rtl.css
|   |   |       bootstrap-grid.rtl.css.map
|   |   |       bootstrap-grid.rtl.min.css
|   |   |       bootstrap-grid.rtl.min.css.map
|   |   |       bootstrap-reboot.css
|   |   |       bootstrap-reboot.css.map
|   |   |       bootstrap-reboot.min.css
|   |   |       bootstrap-reboot.min.css.map
|   |   |       bootstrap-reboot.rtl.css
|   |   |       bootstrap-reboot.rtl.css.map
|   |   |       bootstrap-reboot.rtl.min.css
|   |   |       bootstrap-reboot.rtl.min.css.map
|   |   |       bootstrap-utilities.css
|   |   |       bootstrap-utilities.css.map
|   |   |       bootstrap-utilities.min.css
|   |   |       bootstrap-utilities.min.css.map
|   |   |       bootstrap-utilities.rtl.css
|   |   |       bootstrap-utilities.rtl.css.map
|   |   |       bootstrap-utilities.rtl.min.css
|   |   |       bootstrap-utilities.rtl.min.css.map
|   |   |       bootstrap.css
|   |   |       bootstrap.css.map
|   |   |       bootstrap.min.css
|   |   |       bootstrap.min.css.map
|   |   |       bootstrap.rtl.css
|   |   |       bootstrap.rtl.css.map
|   |   |       bootstrap.rtl.min.css
|   |   |       bootstrap.rtl.min.css.map
|   |   |       
|   |   \---js
|   |           bootstrap.bundle.js
|   |           bootstrap.bundle.js.map
|   |           bootstrap.bundle.min.js
|   |           bootstrap.bundle.min.js.map
|   |           bootstrap.esm.js
|   |           bootstrap.esm.js.map
|   |           bootstrap.esm.min.js
|   |           bootstrap.esm.min.js.map
|   |           bootstrap.js
|   |           bootstrap.js.map
|   |           bootstrap.min.js
|   |           bootstrap.min.js.map
|   |           
|   +---css
|   |       style.css
|   |       
|   +---fontawesome
|   |   |   attribution.js
|   |   |   LICENSE.txt
|   |   |   
|   |   +---css
|   |   |       all.css
|   |   |       all.min.css
|   |   |       brands.css
|   |   |       brands.min.css
|   |   |       fontawesome.css
|   |   |       fontawesome.min.css
|   |   |       regular.css
|   |   |       regular.min.css
|   |   |       solid.css
|   |   |       solid.min.css
|   |   |       svg-with-js.css
|   |   |       svg-with-js.min.css
|   |   |       v4-shims.css
|   |   |       v4-shims.min.css
|   |   |       
|   |   +---js
|   |   |       all.js
|   |   |       all.min.js
|   |   |       brands.js
|   |   |       brands.min.js
|   |   |       conflict-detection.js
|   |   |       conflict-detection.min.js
|   |   |       fontawesome.js
|   |   |       fontawesome.min.js
|   |   |       regular.js
|   |   |       regular.min.js
|   |   |       solid.js
|   |   |       solid.min.js
|   |   |       v4-shims.js
|   |   |       v4-shims.min.js
|   |               
|   +---gen
|   |   |   all.css
|   |   |   all.js
|   |   |   bootstrap.bundle.min.js.map
|   |   |   bootstrap.min.css.map
|   |   |   leaflet.js.map
|   |   |   
|   |   \---images
|   |           layers-2x.png
|   |           layers.png
|   |           marker-icon-2x.png
|   |           marker-icon.png
|   |           marker-shadow.png
|   |           
|   +---images
|   |       elevator.svg
|   |       esc.png
|   |       escalator.svg
|   |       favicon.png
|   |       img_elevators.jpg
|   |       img_subway_station_elevator_doors.jpg
|   |       
|   +---js
|   |       jquery.min.js
|   |       popper.min.js
|   |       scripts.js
|   |       
|   +---leaflet
|   |   |   leaflet-src.esm.js
|   |   |   leaflet-src.esm.js.map
|   |   |   leaflet-src.js
|   |   |   leaflet-src.js.map
|   |   |   leaflet.css
|   |   |   leaflet.js
|   |   |   leaflet.js.map
|   |   |   
|   |   \---images
|   |           layers-2x.png
|   |           layers.png
|   |           marker-icon-2x.png
|   |           marker-icon.png
|   |           marker-shadow.png
|   |           
|   \---webfonts
|           fa-brands-400.eot
|           fa-brands-400.svg
|           fa-brands-400.ttf
|           fa-brands-400.woff
|           fa-brands-400.woff2
|           fa-regular-400.eot
|           fa-regular-400.svg
|           fa-regular-400.ttf
|           fa-regular-400.woff
|           fa-regular-400.woff2
|           fa-solid-900.eot
|           fa-solid-900.svg
|           fa-solid-900.ttf
|           fa-solid-900.woff
|           fa-solid-900.woff2
|           
+---templates
|   |   base.html
|   |   
|   \---pages
|           404.html
|           about.html
|           index.html
|           
```

## Git

[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Github

[GitHub, Inc.](https://github.com/) is a subsidiary of Microsoft which provides hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features.

## GitHub Setup

- …or create a new repository on the command line
```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<yourusername>/open_data_python_mta.git
git push -u origin main
```
- push to repository from the command line
```
git add .
git commit -m "commit message"
git push -u origin main
```

## Deployment

This project is configured to deploy onto [Heroku](https://heroku.com/apps)

### Install the Heroku CLI

Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

### Create a README.md

Basic writing and formatting syntax

Create sophisticated formatting for your prose and code on GitHub with simple syntax.
[Learn more](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

#### README Technical Writer Guide

[Tools for Technical Writers](https://github.com/heyawhite/tech-writing-tools) - A GitHub repository containing lists of suggested tools for technical writers.

## Stay in Touch

[LinkedIn](https://www.linkedin.com/in/jdesire/)