import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement

Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def hello():
    return (
        f"API Routes:<br/>"

        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def hello2():
    
    LastYear=dt.date(2017, 8, 23) - dt.timedelta(days=365)
    Precipitation=session.query(Measurement.date, Measurement.prcp)
    LastYearsPrecipitation=Precipitation.filter(Measurement.date >=LastYear).all()

    return jsonify({date: prcp for date, prcp in Precipitation})

@app.route("/api/v1.0/stations")
def hello3(): 
    LastYear=dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return jsonify(list(np.ravel(session.query(Station.station).all()))
    )

@app.route("/api/v1.0/tobs")
def hello4():
    LastYear=dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return jsonify(list(np.ravel(session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >=LastYear).all())
    ))



if __name__ == '__main__':
    app.run(debug=True)


