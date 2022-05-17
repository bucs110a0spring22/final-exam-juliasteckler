import requests
import json


class Cats:

  def __init__(self):
    """Stores API in self.url
    """
    self.url2 = "https://api.thecatapi.com/v1/images/search"
    
  def getPicts(self):
    """Gets the pictures from the API
    returns picts"""
    r = requests.get(self.url2)
    picts = r.json()
    return picts
    #print(type(picts), picts)


