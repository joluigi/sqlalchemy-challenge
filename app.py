from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd



# Preparing the data with automap to reflect 

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Saving references
Measurement = Base.classes.measurement
Station = Base.classes.station

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
        f"/api/v1.0/startdate<br/><br/>"
        f"To know more about max, min and average temperature from a defined date range go to:<br/> "
        f"/api/v1.0/startdate/enddate <br/>"
        )
@app.route("/api/v1.0/precipitation")
def prcpt():

    # Creating the session
    session = Session(engine)
    # # coverting Dates to datetime type
    # import datetime as dt
    # recent_mth = session.query(func.max(Measurement.date)).all()
    # recent_mth

    # Populating the dataflists with data from the past 12 months
    p_date = {}
    for row in session.query(Measurement).filter(Measurement.date >= '2016-08-23'):
        p_date.update({row.date:row.prcp})

    return jsonify(p_date)
    

if __name__ == "__main__":
    app.run(debug=True)


