import face_rec as fr
import time
import manageFiles as mf

#start = time.time_ns();
#2891021500 ns or 2.8910215 s  to encode one image!
#for 200k images, that is 160.61230556 hours. way too long for us to do.
#encoded = fr.get_encoded_faces()
encoded = fr.get_encoded_faces()
encoding = fr.get_face_encoding_from_path("test.jpg")
encoded["test"] = encoding
mf.saveToPickle(encoded, "encodings")
#interval = time.time_ns()-start
#print(type(encoding))#<class 'numpy.ndarray'>
#print(interval)
#print(encoding)
#print(type(encoded)) <class 'dict'>
#saveToJSON(encoded, 'faces')
