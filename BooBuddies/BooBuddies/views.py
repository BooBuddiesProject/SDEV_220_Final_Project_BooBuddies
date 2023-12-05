"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, url_for
from BooBuddies import app

@app.route('/', methods =["GET",'PUT', "POST"])
@app.route('/home', methods =["GET",'PUT', "POST"])
def home():
    if request.method == "POST":         
       search_string = request.form.get("search-keyword")
       print(search_string)
       return "You searched for: " + str(search_string) 
    
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
