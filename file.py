In jupyter notebook first run these commands step by step
first:
improt cv2
import numpy
photo1 = numpy.zeros([200,200,3])
photo1[:,:]=[0,0,255]

second
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()

third:
photo2=numpy.zeros([200,200,3])
temp=numpy.zeros([200,200,3])
photo2[:100,:100]=[0,255,0]

forth:
cv2.imshow('hi',photo2)
cv2.waitKey()
cv2.destoryAllWindows()

#image crop some part of both image and swap it.
fifth:
for i in range(50,100):
  for j in range(50,150):
    temp[i,j] = photo2[i,j]
    photo2[i,j] = photo1[i,j]
    photo1[i,j] = temp[i,j]
    
sixth:
cv2.imshow('hi',photo1)
cv2.waitKey()
cv2.destroyAllWindows()

# image and combine it to form a single image
seventh:
x = numpy.append(photo1,photo2.axis=1)
cv2.imshow('hi',x)
cv2.waitKey()
cv2.destroyAllWindows()
