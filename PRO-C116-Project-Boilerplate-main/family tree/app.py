# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "shivansh" 
    age = "14"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/f")
def father():
    name = "rajesh"
    age="46"
    return render_template('index.html', name = name , age = age)

# define the route to mother webpage
@app.route("/m")
def mother():
    name = "asha"
    age="44"
    return render_template('index.html', name = name , age = age)


# define the route to friends webpage
@app.route("/fr")
def friends():
    name = "manav"
    age="14"
    return render_template('index.html', name = name , age = age)



# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
