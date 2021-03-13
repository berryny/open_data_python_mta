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

# Software Installation

- [Anaconda](https://www.anaconda.com/) is the birthplace of Python data science.
- [Visual Studio Code](https://code.visualstudio.com/) is a code editor redefined and optimized for building and debugging modern web and cloud applications.
    - Python extension for Visual Studio Code [install](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 
    - [Try Jupyter](https://jupyter.org/try)
    - [Jupyter notebooks with Binder](https://mybinder.org/)

## Quick Start

- Clone the repo:
  ```
  git clone https://github.com/<username>/python-flask-boilerplate.git
  cd python-flask-boilerplate
  ```
- Install Virtual Environment:
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
-  Run the development server:
  ```
  py app.py
  ```
- Navigate to 
    - [http://localhost:5000](http://localhost:5000)
    - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - To stop server Press CTRL+C to quit 

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
git remote add origin https://github.com/berryny/open_data_python_mta.git
git push -u origin main
```
- push to repository from the command line
```
git add .
git commit -m "commit message"
git push -u origin main
```

### Create a README.md

Basic writing and formatting syntax

Create sophisticated formatting for your prose and code on GitHub with simple syntax.
[Learn more](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

#### README Technical Writer Guide

[Tools for Technical Writers](https://github.com/heyawhite/tech-writing-tools) - A GitHub repository containing lists of suggested tools for technical writers.

## Stay in Touch

[LinkedIn](https://www.linkedin.com/in/jdesire/)