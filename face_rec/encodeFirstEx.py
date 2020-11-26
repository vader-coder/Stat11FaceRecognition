import face_rec as fr
import manageFiles.py as mf
path = 'C:/Users/pwhee/Documents/archive/'
identityToImgList = mf.readPickle(path+'imgNames/identityToImgList.pkl')
oneImgList = identityToImgList[0]
twoImgList = identityToImgList[1]
imgs = [oneImgList[0], oneImgList[1], twoImgList]
for img in imgs:
    fr.get_face_encoding_from_path(img)
