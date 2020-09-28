from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt

# create engine
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# step 1:
app = Flask(__name__)

@app.route("/")
def helloWorld():
    #  urls that tell the user the end points that are available
    return ("Hello World<br>"    
    f"These are the available pages:<br>"
    f"/precipitation<br>"
    f"/stations<br>"
    f"/tobs<br>"
    f"/start date as YYYY-MM-DD <br>"
    f"/start date as YYYY-MM-DD/end date as YYYY-MM-DD<br>")

@app.route("/precipitation")
def precipitation():
    # create our session link from Python to the DB
    session = Session(engine)
    lastdayInDB=dt.date(2017,8,23)
    lastdayminusOneYear = lastdayInDB - dt.timedelta(days=365)
    lastyearsResults = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= lastdayminusOneYear).all()
    print(lastyearsResults)
    session.close()

# convert the query results to a dictionary using 'date' as the key and 'prcp' as the value.
# return the JSON representation of your dictionary

    results = []
    for date, prcp in lastyearsResults:
        result_dict = {}
        result_dict[date] = prcp
        results.append(result_dict)
    return jsonify(results)
        
@app.route("/stations")
def stations():
    session = Session(engine)
    # return a list of all the stations in JSON format
    listOfStations = session.query(Station.station).all() 
    session.close()
    stationOneDimension = list(np.ravel(listOfStations))
    return jsonify(stationOneDimension)
    
@app.route("/tobs")
def tobs():
    session = Session(engine)
    lastdayInDB=dt.date(2017,8,23)
    lastdayminusOneYear = lastdayInDB - dt.timedelta(days=365)
    
    # Find the most active station
    mostactivestation = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count().desc()).first()
    # Get the station id of the most active station
    (mostactivestationid, ) = mostactivestation
    print(f"The station id of the most active station is {mostactivestation}.")

    # Query to retrieve the temperatures fro the most active station from the last year
    lastyearResults = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == mostactivestationid).\
        filter(Measurement.date >= lastdayminusOneYear).all()
    session.close()

    # Convert the query result to a dictionary using date as the key and temperature as the value
    temperatures = []
    for date, temp in lastyearResults:
        if temp != None:
            temp_dict = {}
            temp_dict[date] = temp
            temperatures.append(temp_dict)
    # Return the JSON representation of dictionary
    return jsonify(temperatures)

@app.route('/<start>', defaults={'end': None})
@app.route('/<start>/<end>')
def findtemperaturesfordaterange(start, end):
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a give date range
    # When given the start date only, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    # When given the start and end dates, calculate the TMIN, TAVG, and TMAX for the dates between the start and end dates inclusive

    session = Session(engine)
    # if both a start date and end date are known
    if end != None:
        temperatures = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # If only the start date is known
    else:
        temperatures = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()
    session.close()

    # Convert the queries results to lists
    temperatures_list = []
    no_temperature_data = False
    for min_temp, avg_temp, max_temp in temperatures:
        if min_temp == None or avg_temp == None or max_temp == None:
            no_temperature_data = True
        temperatures_list.append(min_temp)
        temperatures_list.append(avg_temp)
        temperatures_list.append(max_temp)
    # Return the JSON representation of the temperature dictionary
    if no_temperature_data == True:
        return f"No temperature data found for the given date range. Try another date range."
    else:
        return jsonify(temperatures_list)

#2nd step:

if __name__ == '__main__':
    app.run()