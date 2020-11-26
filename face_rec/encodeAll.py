#encode all images
import manageFiles as mf
import face_rec as fr
from collections import deque

imgNamesList = mf.readJSON('imgNamesList')

#enables us to encode a range of images
#ex; pass in first half of image name list to fnames and 0 to offset
#for latter half, pass in second half of image name list to fnames and the index of the first image in
#the latter half inside imgNamesList
def encodeRange(fnames, offset):
    errorList = deque([])
    otherErrorList = deque([])
    encoded = {}
    for index, f in enumerate(fnames):
        try:
            if f.endswith(".jpg") or f.endswith(".png"):
                path = 'C:/Users/pwhee/Documents/archive/img_align_celeba/'+f
                encoded[f] = fr.get_face_encoding_from_path(path, errorList, index+offset)
        except:
            otherErrorList.append(index+offset)
    return (encoded, errorList, otherErrorList)


half = len(imgNamesList)//2
encoded1, eList1, eOList1 = encodeRange(imgNamesList[:half], 0)
mf.saveToPickle(encoded1, 'encoded1')
mf.saveToPickle(eList1, 'errorList1')
mf.saveToPickle(eOList1, 'otherErrorList1')
#test for 1st 4
"""
encoded, eList, eOList = encodeRange(imgNamesList[:4], 0)
print(encoded)
print(eList)
print(eOList)
mf.saveToPickle(encoded, 'imgNamesToEncoding')
mf.saveToPickle('eList', 'errorList')
mf.saveToPickle(eOList, 'otherErrorList')
"""
"""
half = len(imgNamesList)//2
encoded1, eList1, eOList1 = encodeRange(imgNamesList[:half], 0)
encoded2, eList2, eOList2 = encodeRange(imgNamesList[half:], half)
"""
