
"""
Routes and views for the flask application.
"""

import pandas as pd
from datetime import datetime
from flask import render_template, request, url_for
from BooBuddies import app
from .data import foodtypes_list, search_Cuisine
from . import recommendations, dataframe, geolocate

@app.route('/', methods =["GET",'PUT', "POST"])
@app.route('/home', methods =["GET",'PUT', "POST"])
def home():
    # This pulls the list of food types to be selected from data\foodtypes.csv
    foodtypelist= foodtypes_list()
   
    # This kicks off the search
    if request.method == "POST":   
       search_FoodType=request.form.get("search_Foodtype")
       search_City = request.form.get("search_City")
       search_State = request.form.get("search_State")

       return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        foodtypes= foodtypelist,
        sel_Foodtype=search_FoodType,
        sel_City=search_City,
        sel_State=search_State,
    )
    
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        foodtypes= foodtypelist,
    )



@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='For more information:'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='This site is designed to help you find food based on type near you.'
    )

@app.route('/search')
def search():
    """Renders the search results."""
    args = request.args
    df = dataframe.DataFrame()
    search_term = args.get("search-City", "") + "," + args.get("search-State", "")
    p1 = geolocate.Geolocation(search_term).p1
    results = recommendations.get_recs(df, args, p1)
    return render_template(
        'search.html',
        title='Search',
        year=datetime.now().year,
        results = results
    )
