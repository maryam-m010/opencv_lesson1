import cv2
a = cv2.imread("pikachu.png", 1)
cv2.imshow("hello", a)
cv2.waitKey(0)
cv2.destroyAllWindows()

b = cv2.imread("pikachu.png", 0)
cv2.imshow("hello", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

c = cv2.imread("pikachu.png", -1)
cv2.imshow("hello", c)
cv2.waitKey(0)
cv2.destroyAllWindows()

# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
path1 = r"C:\\Users\\mmary\\OneDrive - Queen Mary, University of London\\Maryam\\coding\\Jet Learn\\open cv\\pikachu.png"
path2 = r"C:\\Users\\mmary\\OneDrive\\Desktop"

import os
print(os.listdir(path2)) #listdirectory
os.chdir(path2) #change directory
image = cv2.imread(path1)
cv2.imwrite("pikachu.png", image)
