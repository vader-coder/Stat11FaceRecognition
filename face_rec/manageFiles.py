import pickle as pkl
import json

#file to define functions useful for reading and writing to filefs

def saveToJSON(object, filename):
    with open(filename+'.json', 'w') as output:
        json.dump(object, output)

def readJSON(filename):
    with open(filename+'.json', 'r') as output:
        return json.load(output)

def saveToPickle(object, filename):
    with open(filename+'.pkl', 'wb') as output:
        pkl.dump(object, output, pkl.HIGHEST_PROTOCOL)

def readPickle(filename):
    with open(filename+'.pkl', 'rb') as input:
        return pkl.load(input)
