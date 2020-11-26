import manageFiles as mf

#list want a dictinary of identities to names, names to identities, and just a name list
with open('identity_CelebA.txt') as f:
    imgToIdentity = {}
    identityToImgList = {}
    imgNamesList = []
    identityList = []
    for line in f:
        vals = line.split(' ')
        imgName = vals[0]
        identity = int(vals[1])
        if (identity in identityToImgList):
            identityToImgList[identity].append(imgName)
        else:
            identityToImgList[identity] = [imgName]
        imgToIdentity[imgName] = identity
        imgNamesList.append(imgName)
        identityList.append(identity)
    mf.saveToJSON(imgToIdentity, 'imgToIdentity')
    mf.saveToJSON(identityToImgList, 'identityToImgList')
    mf.saveToJSON(imgNamesList, 'imgNamesList')
    mf.saveToJSON(identityList, 'identityList')

    mf.saveToPickle(imgToIdentity, 'imgToIdentity')
    mf.saveToPickle(identityToImgList, 'identityToImgList')
    mf.saveToPickle(imgNamesList, 'imgNamesList')
    mf.saveToPickle(identityList, 'identityList')
