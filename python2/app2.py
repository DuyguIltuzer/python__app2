
##import our libraries
from flask import Flask, render_template

#instantiating the app object
app2 = Flask(__name__)


pet_1 =[{
    "Name": "Spotty",
    "Breed": "Cat",
    "Age" : 3,
    "Type": "Sokoke"
}]

Pets =  [ "Spotty", "Milton", "Ted"]

pet_list= [{
    "Name": "Spotty",
    "Breed": "Cat",
    "Age" : 3,
    "Type": "Sokoke"},
    {
    "Name": "Milton",
    "Breed": "Cat",
    "Age": 4,
    "Type": "Cobby"
        }
    
    ]

#create our first route
@app2.route("/")
def hello():
    return render_template("index.html", pet_list=pet_list)




if __name__== "__main__":
    app2.run(
        debug = True,
        port = 3000
    )