import requests

#function is to get information from WeatherStackAPI 
def get_weather():
    # api_key = '25c8075700176ffa23836cc6b6820d56'
    try:
        #r = requests.get('http://api.weatherstack.com/current?access_key=25c8075700176ffa23836cc6b6820d56&query=Hamilton')
        r = 0
        data = r.json()
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]
    
    except:
        temperature = 22
        weather_description = 'sunny'
        ## API key only allows 100 uses which quickly get used up within a matter of 100 seconds 
        ## Source: WeatherStackAPI and fetch another key if needed 
        ## As well, these are the possible outputs of weather_description:
        ## "clear sky", "few clouds", "scattered clouds", "broken clouds", "overcast clouds", "shower rain", "rain", "heavy rain", "light rain", "snow", "heavy snow", "sleet", "hail", "thunderstorm", "mist", "fog", "haze", and "dust"

    return temperature ,weather_description

