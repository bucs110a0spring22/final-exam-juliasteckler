import requests
import dog
import cat
import random

def main():
  
  choices = input("Would you like to see a dog or cat?: ")
  if choices=="dog":
    doge = dog.Dogs()
    hey = doge.getPics()
    print(hey)

  if choices=="cat":
    kitty = cat.Cats()
    hi = kitty.getPicts()
    print(hi)

  randomy = input("Wanna another one picked by us? :)  ")  
  if randomy=="no":
    print("Okay >:(")

  if randomy=="yes":
    kitty = cat.Cats()
    hi = kitty.getPicts()
    doge = dog.Dogs()
    hey = doge.getPics()
    mylist = [hi, hey]
    print(random.choice(mylist))

    
main()