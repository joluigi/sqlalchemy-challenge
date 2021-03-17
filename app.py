from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print('Everything executed correctly')
    return(
        f"Hello welcome to the Station temperature API<br/><br/>"
        f"Here is a list of available routes:<br/><br/>"
        f"To obtain the precipitation data type:<br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        f"To obtain data about stations go to:<br/> "
        f"/api/v1.0/stations<br/><br/>"
        f"If you want to know the temperature observations from the most recurrent stations go to:<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"To know more about max, min and average temperature from a define start date go to:<br/> "
        f"/api/v1.0/<start><br/><br/>"
        f"To know more about max, min and average temperature from a defined date range go to:<br/> "
        f"/api/v1.0/<start>/<end><br/>"
        )
   

if __name__ == "__main__":
    app.run(debug=True)


