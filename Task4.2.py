crop1=np.copy(photo1[110:170,220:280])
crop2=np.copy(photo2[126:186,220:280])
#display crop photo1
cv2.imshow('hi',crop1)
cv2.waitKey()
cv2.destroyAllWindows()
#display crop photo2
cv2.imshow('hi',crop2)
cv2.waitKey()
cv2.destroyAllWindows()
