import json

from django.http import JsonResponse
from django.shortcuts import render

from planets.models import Planet
from swapi.api import get_planet_by_id

def get_by_id(request, id):
    try:
        planet = Planet.objects.get(pk=id)
    except Planet.DoesNotExist as dne:
        success, response = get_planet_by_id(id)
        planet = Planet(
            planet_id=id,
            name=response['name'],
            diameter=int(response['diameter']),
            rotation_period=int(response['rotation_period']),
            orbital_period=int(response['orbital_period']),
            gravity=response['gravity'],
            population=int(response['population']),
            climate=response['climate'],
            terrain=response['terrain'],
            surface_water=int(response['surface_water'])
        )
        planet.save()      
    return JsonResponse(planet.to_dict(), status=200)

# search by population
def get_planet_by_pop(request, population):
    try:
        planets = Planet.objects.filter(population=population)
        for planet in planets:
            planet = planet.to_dict()
            return JsonResponse(planet, status=200)
    except ValueError:
        print("There are no planets with that population")

    
    
    
        

    