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