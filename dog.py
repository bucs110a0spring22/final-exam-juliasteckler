import requests
import json

class Dogs:

  def __init__(self):
    """Stores API in url
    """
    self.url = "https://dog.ceo/api/breeds/image/random"
    
  def getPics(self):
    """Gets the pictures from the API
    returns pics"""
    r = requests.get(self.url)
    pics = r.json()
    return pics
    #print(type(pics), pics)