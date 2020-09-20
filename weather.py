#! python3
# weather.py
# AUTHOR - Joy Samaddar

# Enter your OpenWeatherMap APPID below
APPID = 'Enter APPID HERE'

import json, requests, sys, time
from win10toast import ToastNotifier

if len(sys.argv)<2:
    location = input('Enter the location (City name, 2-Letter Country Code): ');
else:
    location =  ''.join(sys.argv[1:])

while True:
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+APPID+'&units=metric'
    response = requests.get(url)

    response.raise_for_status()

    data = json.loads(response.text)

    result = '''
Temperature: {} °C
Weather: {}
    '''.format(data['main']['temp'], data['weather'][0]['main'])

    toaster = ToastNotifier()

    toaster.show_toast("Todays weather in "+location+"!", result, threaded=True,
                       icon_path=None, duration=3)

    import time
    while toaster.notification_active():
        time.sleep(0.1)

    time.sleep(86400)


