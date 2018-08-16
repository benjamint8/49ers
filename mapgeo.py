from geopy.geocoders import Nominatim

def get_location(uni):
  a = "University of"
  b = "University"
  geolocator = Nominatim(user_agent="my_map")
  location = geolocator.geocode(uni)
  location2 = geolocator.geocode(a + uni)
  location3 = geolocator.geocode(uni + b)

  if location is not None:
    return(location)
  elif location2 is not None:
    return(location2)
  else:
    return(location3)


lat_long_dict = {}

#loop the dictionary
for player , university in players_uni_dict.items():
    try:
    	#Run the get_location function that we wrote
    	#and save it in location
        location = get_location(university)
        #declaring another empty dictionary
        lat_long = {}
        #Save the latitude in the lat_long dictionary as latitude
        lat_long["latitude"] = location.latitude
        #Save the longitude into lat_long dictionary as longitude
        lat_long["longitude"] = location.longitude
        #Save lat_long into lat_long_dict
        lat_long_dict[player] = lat_long
    except Exception as e:
        continue

        print(lat_long_dict)

pp = pprint.PrettifyPrinter(indent=4)
pp.pprint·lat_long_dict)

import csv
import plotly.plotly as py

import plotly
plotly.tools.set_credentials_file(username='<YungBuckUpNext>', api_key='<vHbW9x9M2nMMMj3Zbrhn>')
'player_lat_long = pd.read_csv('player_file.csv')
data = [dict(
    type = 'scattergeo',
        locationmode = 'USA-states',
        lon = player_lat_long['Longitude']
        lat = player_lat_long['Latitude']
        text = player_lat_long['Player'] + ' ' + player_lat_long['Location'],
        )]
layout = dict(
    title = '49ers',
    geo= dict(
        scope='usa',
        projection=dict( type='albers usa' ),
        showland = True
        landcolor= "rgb(250, 250, 250)",
        subunitcolor = "rgb(217, 217, 217)",
        countrycolor = "rgb(217, 217, 217)",
        countrywidth = 0.5,
        subunitwidth = 0.5

    )
)
