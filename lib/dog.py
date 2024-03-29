#!/usr/bin/env python3

from typing import Any
import random


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Nimbus", breed=random.choice(APPROVED_BREEDS)):
        ## Using the public property var as opposed to the internal _var for validations to occur during object initialization
        self.name = name
        self.breed = breed

    def getName(self):
        # print("retrieving name")
        return self._name    
    
    def setName(self, name):
        # print("setting name")
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name 
        else: 
            print("Name must be string between 1 and 25 characters.")
    
    name = property(getName, setName)
    
    def getBreed(self):
        # print("retrieving name")
        return self._breed    
    
    def setBreed(self, breed):
        # print("setting name")
        if type(breed) == str and breed in APPROVED_BREEDS:
            self._breed = breed 
        else: 
            print("Breed must be in list of approved breeds.")
    
    breed = property(getBreed, setBreed)
    
    
    def __repr__(self):
        return f"{self.name} the Dog is a {self._breed}"

fido = Dog("fido")
fido.name = 66
# print(type(fido) == Dog)