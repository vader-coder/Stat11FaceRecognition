import manageFiles as mf

encoded = {}
encod = mf.readPickle('encodings')
print(type(encod['imageNameList']))
"""
encoded['imageNameToEncoding'] = encod
#save corresponding keys and values for later
encoded['imageNameList'] = list(encod.keys())
encoded['encodingList'] = list(encod.values())
"""
#mf.saveToPickle(encoded, 'encodings')
#print(encod)
