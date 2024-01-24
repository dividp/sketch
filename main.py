import cv2
image = cv2.imread("tiger.jpeg")
cv2.imshow("Given Picture", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Step1 : GrayScale", gray_image)
cv2.waitKey(0)
inverted_image = 255 - gray_image
cv2.imshow("Step 2: Invert", inverted_image)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Step3: Sketch", pencil_sketch)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
outlines = cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=outlines)

cv2.imshow("Original Image", image)
cv2.imshow("Outlines", outlines)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
