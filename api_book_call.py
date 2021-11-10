#!/usr/bin/env python3

import os
import json;
import requests

api_token = 'api_key'

option_to_choice=input("Please set the option whcih you want to choose by searching the movie.\n[1] Search the movie by the name (put `1` )\n[2] Search the movie by the ID rom OMDb API (put `2`)\nPlease Choose the option 1 or 2 : ")

class APIApp:
   def __init__(self, api_token):

      self.api_token = api_token


   # Thsi method use to find the movie via movie name is using request module and metod get
   def get_movie_by_name(self,):


      movie_name=str(input("Please provide the movie name: "))
      plot_value = str(input("If you want to display full information about the movie put the word `full` otherewise put the `short`: "))

      response = requests.get("https://www.omdbapi.com/?t="+movie_name+"&plot="+plot_value+"&apikey="+self.api_token).json()
      print(json.dumps(response, sort_keys=True, indent=4))

# Thsi method use to find the movie via movie id is using request module and metod get
   def get_movie_by_id(self):

      movie_id = input("Please provide the movie id from OMDb API: ")
      plot_value = str(input("If you want to display full information about the movie put the word `full` otherewise put the `short`: "))

      response = requests.get("https://www.omdbapi.com/?i="+movie_id+"&plot="+plot_value+"&apikey="+self.api_token).json()
      print(son.dumps(response, sort_keys=True, indent=4))

# object of the class
movie_object = APIApp(api_token)

# set up option for finding the movie via specific id.
if option_to_choice == "1":
   movie_object.get_movie_by_name()
elif option_to_choice == "2":
   movie_object.get_movie_by_id()
else:
   print("The option whcih you choose was incorrected:")

