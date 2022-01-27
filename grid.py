import numpy as np
import cv2
from math import floor, ceil

def draw_grid(img, grid_shape, color=(0, 255, 0), thickness=1):
	h, w, _ = img.shape
	rows, cols = grid_shape
	dy, dx = h / rows, w / cols

    # draw vertical lines
	for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
		x = int(round(x))
		cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)

	# draw horizontal lines
	for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
		y = int(round(y))
		cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)

	return img

def get_perbandingan(img, grid_shape):
	h, w, _ = img.shape
	rows, cols = grid_shape
	pr = floor(h / rows)
	pc = floor(w / cols)
	return (pr, pc)

def pixel2rect(pixel, banding):
	x, y = pixel
	bx, by = banding
	rx = floor(x/bx)
	ry = floor(y/by)
	return (rx, ry)

def rect2pixel(rect, banding):
	x, y = rect
	bx, by = banding
	px = x * bx
	py = y * by
	return (px, py)

def get_blue_object(img):
	pxx = 0
	pyy = 0
	hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	blue_lower = np.array([94, 80, 2], np.uint8)
	blue_upper = np.array([120, 255, 255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

	kernal = np.ones((5, 5), "uint8")
	blue_mask = cv2.dilate(blue_mask, kernal)

	contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#for pic, contour in enumerate(contours):
	area = cv2.contourArea(contours[0])
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contours[0])
		pxx = floor((w/2) + x)
		pyy = floor((h/2) + y)
	
	return (pxx, pyy)

imageFrame = cv2.imread("obj.PNG")
imageFrame = draw_grid(imageFrame, (21, 21), (0, 255, 255), 1)

banding = get_perbandingan(imageFrame, (21, 21))
pospixel = get_blue_object(imageFrame)
posrect = pixel2rect(pospixel, banding)

randompixel = rect2pixel((2,2), banding)
rpx, rpy = randompixel
bx, by = banding

print("size image: ", imageFrame.shape)
print("banding: ", banding)
print("blue in pixel: ", pospixel)
print("blue in rect: ", posrect)
print("random pixel: ", randompixel)

imageFrame = cv2.rectangle(imageFrame, pospixel, pospixel, (0, 255, 0), 5)
imageFrame = cv2.rectangle(imageFrame, randompixel, (rpx + bx , rpy + by), (0, 255, 0), 5)

while(1):
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break