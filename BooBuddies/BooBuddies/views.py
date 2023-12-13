<<<<<<< HEAD
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, url_for
from BooBuddies import app
from .dataload import foodtypes_list


@app.route('/', methods =["GET",'PUT', "POST"])
@app.route('/home', methods =["GET",'PUT', "POST"])
def home():
    # This kicks off the search
    if request.method == "POST":   
       search_FoodType=request.form.get("search_Foodtype")
       search_City = request.form.get("search-City")
       search_State = request.form.get("search-State")
       search_Country = request.form.get("search-Country")
       search_string=search_City + " " + search_State + " " + search_Country + " " + search_FoodType
       return "You searched for: " + str(search_string) 
    
    foodtypelist= foodtypes_list()
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
        message='This site is under construction...'
    )

@app.route('/search')
def search():
    """Renders the about page."""
    return render_template(
        'search.html',
        title='Search',
        year=datetime.now().year,
        message='This site is under construction...'
    )
=======
"""
Routes and views for the flask application.
"""
import pandas as pd
from datetime import datetime
from flask import render_template, request, url_for
from BooBuddies import app

@app.route('/', methods =["GET",'PUT', "POST"])
@app.route('/home', methods =["GET",'PUT', "POST"])
def home():
    if request.method == "POST":         
        search_string = request.form.get("search-keyword")

        #search_list should be the filters used to find what type of restaurant
        search_list = ['afghan', 'african', 'american', 'armenian', 'asian', 'australian', 'austrian', 'bagels', 'bakery', 'bar', 'barpubbrewery', 'barbecue', 'basque', 'brazilian', 'breakfastbrunch', 'british', 'burgers', 'burmese', 'cafecoffeeshop', 'cafeteria', 'cajuncreole', 'california', 'caribbean', 'chinese', 'contemporary', 'continentaleuropean', 'delisandwiches', 'desserticecream', 'diner', 'dutchbelgian', 'easterneuropean', 'ethiopian', 'family', 'fastfood', 'finedining', 'french', 'game', 'german', 'greek', 'hotdogs', 'international', 'italian', 'japanese', 'juice', 'korean', 'latinamerican', 'mediterranean', 'mexican', 'mongolian', 'organichealthy', 'persian', 'pizzeria', 'polish', 'regional', 'seafood', 'soup', 'southern', 'southwestern', 'spanish', 'steaks', 'sushi', 'thai','turkish', 'vegetarian', 'vietnamese']

        def search_Cuisine():
            df = pd.read_csv("Restaurant/chefmozcuisine.csv")
    
            filtered_df = df["Rcuisine"] 

            nomatch = "No Match Was Found"

            for item in df:
                if item == search_string:
                    search_result = item
                    noresult = "False"
                    return search_result
                    
                else:
                    noresult = "True"
                    continue

            if noresult == "True":
                search_result = nomatch
                print(search_result)
                    
            else:
                print(search_result)

        return search_Cuisine()
    
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


# @app.route('/', methods =["GET", "POST"])
# def gfg():

#        # getting input with name = fname in HTML form
#        search_string = request.form.get("search-field")
       
#        return "Your name is "+first_name + last_name
#     return render_template("form.html")

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
        message='This site is under construction...'
    )

@app.route('/search')
def search():
    """Renders the about page."""
    return render_template(
        'search.html',
        title='Search',
        year=datetime.now().year,
        message='This site is under construction...'
    )
>>>>>>> 29ff6d27acdb1375d088ccbdd415f7c0f1b6ef44
