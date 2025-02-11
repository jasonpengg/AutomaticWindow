import requests

def get_weather():
    api_key = '25c8075700176ffa23836cc6b6820d56'
    location = 'Hamilton'
    temperature = 0
    weather_description = 'sunny'
    return temperature ,weather_description
'''
    r = requests.get('http://api.weatherstack.com/current?access_key=25c8075700176ffa23836cc6b6820d56&query=Hamilton')

    data = r.json()
    print(data)
    temperature = data['current']['temperature']
    weather_description = data['current']['weather_descriptions'][0]
    '''
