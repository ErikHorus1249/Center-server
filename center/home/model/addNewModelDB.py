from home.models import *

def addNewModel(url, ver):
    new_model = DLModel(modelUrl=url, modelVersion=ver)
    new_model.save

# def removeOldModel(ver):
    
