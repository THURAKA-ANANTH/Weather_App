from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_weather(request):
    city_name = request.query_params.get('cityName')
    if not city_name:
        return Response({"error": "City name is required."}, status=400)
    
    api_key = 'df67e77d4fd049bf1195d54a086f71ad'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return JsonResponse(data)
    else:
        return Response(data, status=response.status_code)
