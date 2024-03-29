#!/usr/bin/env python3
import random 
approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

class Person:
    
    
    def __init__(self, name="Rick", job=random.choice(approved_jobs)):
        
        # set the property as this will call our validation methods getName and setName to confirm the values we want are being used to create new instances
        self.name = name
        self.job = job

    def getName(self):
        # print("retrieving name")
        return self._name    
    
    def setName(self, name):
        # print("setting name")
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name.title()
        else: 
            print("Name must be string between 1 and 25 characters.")
    
    name = property(getName, setName)
    
    def getJob(self):
        return self._job    
    
    def setJob(self, job):
        if job in approved_jobs:
            self._job = job
        else: 
            print("Job must be in list of approved jobs.")
    
    job = property(getJob, setJob)
    
    def __repr__(self):
        return f"{self.name} the Person works in {self.job}"
    
phil = Person()
print(phil)