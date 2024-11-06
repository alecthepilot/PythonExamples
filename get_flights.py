import requests

params = {
  'access_key': '',
  'dep_icao': 'EGKK',
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
print (api_response)

for flight in api_response['data']:
    if 'airline' in flight:
        # if (flight['airline']['name'] == 'British Airways'):
        print("Airline: " + flight['airline']['name'])
        print("Departing From: " + flight['departure']['airport'])
        print("Estimated departure time: " + flight['departure']['estimated'])
        print("Arriving: " + flight['arrival']['airport'])
        # print("Flight Number: " + flight['flight']['number'])
        print("IATA: " + flight['flight']['iata'])
        print("Flight Date: " + flight['flight_date'])
        print("\n")


            # Query more data about the flight via another API call
