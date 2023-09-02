import requests
import json
import datetime as dt
import taosrest

# get the data from the API
def get_weather(location, conn):

    # Create your key and replace mine with it
    payload = {'Key': '216c55e6b79544339b613615232208', 'q': location, 'aqi': 'yes'}
    r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)

    # Get the json from the request's result
    r_string = r.json()

    # Take only the current part of the JSON
    current = r_string['current']
    #print(current)

    # Fix time format from YYYY-MM-DD hh:mm:ss to -> YYYY-MM-DDThh:mm:ssZ
    # create datetime object from string
    origin_time = dt.datetime.strptime(current['last_updated'],'%Y-%m-%d %H:%M') 
    
    #turn datetime into formated string for tdengine
    # Keep in mind this will create timestamps in zulu time. The api only sends you local time.
    # We should fix this, but I can't be bothered right now
    current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    #print(current['last_updated'])

    #print(current)  
    # write the weather data to tdengine
    write_weather(location,current,conn)    

    # we don't need this right now, but I kept it
    return current

#open tdengine connection
def open_con():
 
    # Open a connection to tdengine cloud. Use the url and token specified in the instance
    try:
        conn = taosrest.connect(url="https://gw.us-east.azure.cloud.tdengine.com",
                    token="74471da90c678dc9ba70fc59f93c53fdd59bbf8f"
                    )
 
    except taosrest.Error as e:
        print("error message 1"+ e.errno + "error message 2" + e.msg + "error message 3" + e.status)

    return conn

# Writes the weather data to tdengine
def write_weather(location, weather_js, conn):
    
    # Remove the whitespaces from the locations (tdengine tables don't have whitespaces -> "sanfrancisco" instead of "san francisco")
    no_whitepsace_location = location.replace(" ", "")

    # For debugging    
    # print(no_whitepsace_location)

    # write measurement to tdengine
    conn.query(f"insert into weather.{no_whitepsace_location} values ('{weather_js['last_updated']}', {weather_js['temp_f']}, {weather_js['feelslike_f']}, {weather_js['precip_in']}, {weather_js['wind_mph']})")     
    
# closes the tdengine connection
def close_con(conn):
    conn.close()



if __name__ == "__main__":
    
    # open connection
    conn = open_con()
    
    # write data for cuenca
    get_weather("cuenca",conn)

    # write data for cartagena
    get_weather("cartagena",conn)

    # close connection and end the program
    close_con(conn)
