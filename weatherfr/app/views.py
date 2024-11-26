from django.shortcuts import render
import requests
# Create your views here.
def main(req):
    city_name='kochi'
    if req.method=='POST':
        city_name=req.POST['city']
        api_key='360e4bc3865e745ec844bd7ec054ca11'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        try:
            data=requests.get(url)
            weather_data=data.json()
            data={
                'city':city_name,
                'weather_dis':weather_data['wether'][0]['description']
            }
        except:
            city_name='kochi'

    api_key='360e4bc3865e745ec844bd7ec054ca11'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    data=requests.get(url)
    weather_data=data.json()
    data={
            'city':city_name,
            'weather_dis':weather_data['weather'][0]['description']
            }
    print(weather_data)
    return render(req,'index.html',{'data':data})

