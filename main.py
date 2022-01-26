import cv2
import numpy as np
import imutils
import math
import requests


def nothing(x):
    pass


# variable aksi
walk = 0

# variable url
url = 'http://192.168.4.1/?State='

# variable camera
camera = cv2.VideoCapture(0)

# koordinat
x_bola = 0
y_bola = 0

x_robot_front = 0
y_robot_front = 0

x_robot_back = 0
y_robot_back = 0

# variable bola
l_h_bola = 22
l_s_bola = 93
l_v_bola = 0
u_h_bola = 32
u_s_bola = 255
u_v_bola = 255

cv2.namedWindow("Trackbars_bola")
cv2.createTrackbar("L - H", "Trackbars_bola", l_h_bola, 22, nothing)
cv2.createTrackbar("L - S", "Trackbars_bola", l_s_bola, 93, nothing)
cv2.createTrackbar("L - V", "Trackbars_bola", l_v_bola, 0, nothing)
cv2.createTrackbar("U - H", "Trackbars_bola", u_h_bola, 45, nothing)
cv2.createTrackbar("U - S", "Trackbars_bola", u_s_bola, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars_bola", u_v_bola, 255, nothing)


def getTrackbarBola():
    global l_h_bola, l_s_bola, l_v_bola, u_h_bola, u_s_bola, u_v_bola

    l_h_bola = cv2.getTrackbarPos("L - H", "Trackbars_bola")
    l_s_bola = cv2.getTrackbarPos("L - S", "Trackbars_bola")
    l_v_bola = cv2.getTrackbarPos("L - V", "Trackbars_bola")

    u_h_bola = cv2.getTrackbarPos("U - H", "Trackbars_bola")
    u_s_bola = cv2.getTrackbarPos("U - S", "Trackbars_bola")
    u_v_bola = cv2.getTrackbarPos("U - V", "Trackbars_bola")

    # print("l_h_b : "+str(l_h_bola))
    # print("l_s_b : "+str(l_s_bola))
    # print("l_v_b : "+str(l_v_bola))
    # print("u_h_b : "+str(u_h_bola))
    # print("u_s_b : "+str(u_s_bola))
    # print("u_v_b : "+str(u_v_bola))


# variable robot
l_h_robot_front = 0
l_s_robot_front = 161
l_v_robot_front = 0
u_h_robot_front = 11
u_s_robot_front = 229
u_v_robot_front = 255

l_h_robot_back = 56
l_s_robot_back = 123
l_v_robot_back = 0
u_h_robot_back = 103
u_s_robot_back = 174
u_v_robot_back = 255

cv2.namedWindow("Trackbars_robot_front")
cv2.createTrackbar("L - H", "Trackbars_robot_front",
                   l_h_robot_front, 255, nothing)
cv2.createTrackbar("L - S", "Trackbars_robot_front",
                   l_s_robot_front, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars_robot_front",
                   l_v_robot_front, 0, nothing)
cv2.createTrackbar("U - H", "Trackbars_robot_front",
                   u_h_robot_front, 255, nothing)
cv2.createTrackbar("U - S", "Trackbars_robot_front",
                   u_s_robot_front, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars_robot_front",
                   u_v_robot_front, 255, nothing)


def getTrackbarRobotFront():
    global l_h_robot_front, l_s_robot_front, l_v_robot_front, u_h_robot_front, u_s_robot_front, u_v_robot_front

    l_h_robot_front = cv2.getTrackbarPos("L - H", "Trackbars_robot_front")
    l_s_robot_front = cv2.getTrackbarPos("L - S", "Trackbars_robot_front")
    l_v_robot_front = cv2.getTrackbarPos("L - V", "Trackbars_robot_front")

    u_h_robot_front = cv2.getTrackbarPos("U - H", "Trackbars_robot_front")
    u_s_robot_front = cv2.getTrackbarPos("U - S", "Trackbars_robot_front")
    u_v_robot_front = cv2.getTrackbarPos("U - V", "Trackbars_robot_front")

    # print("l_h_r_f : "+str(l_h_robot_front))
    # print("l_s_r_f : "+str(l_s_robot_front))
    # print("l_v_r_f : "+str(l_v_robot_front))
    # print("u_h_r_f : "+str(u_h_robot_front))
    # print("u_s_r_f : "+str(u_s_robot_front))
    # print("u_v_r_f : "+str(u_v_robot_front))


cv2.namedWindow("Trackbars_robot_back")
cv2.createTrackbar("L - H", "Trackbars_robot_back",
                   l_h_robot_back, 56, nothing)
cv2.createTrackbar("L - S", "Trackbars_robot_back",
                   l_s_robot_back, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars_robot_back", l_v_robot_back, 0, nothing)
cv2.createTrackbar("U - H", "Trackbars_robot_back",
                   u_h_robot_back, 140, nothing)
cv2.createTrackbar("U - S", "Trackbars_robot_back",
                   u_s_robot_back, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars_robot_back",
                   u_v_robot_back, 255, nothing)


def getTrackbarRobotBack():
    global l_h_robot_back, l_s_robot_back, l_v_robot_back, u_h_robot_back, u_s_robot_back, u_v_robot_back

    l_h_robot_back = cv2.getTrackbarPos("L - H", "Trackbars_robot_back")
    l_s_robot_back = cv2.getTrackbarPos("L - S", "Trackbars_robot_back")
    l_v_robot_back = cv2.getTrackbarPos("L - V", "Trackbars_robot_back")

    u_h_robot_back = cv2.getTrackbarPos("U - H", "Trackbars_robot_back")
    u_s_robot_back = cv2.getTrackbarPos("U - S", "Trackbars_robot_back")
    u_v_robot_back = cv2.getTrackbarPos("U - V", "Trackbars_robot_back")

    # print("l_h_r_b : "+str(l_h_robot_back))
    # print("l_s_r_b : "+str(l_s_robot_back))
    # print("l_v_r_b : "+str(l_v_robot_back))
    # print("u_h_r_b : "+str(u_h_robot_back))
    # print("u_s_r_b : "+str(u_s_robot_back))
    # print("u_v_r_b : "+str(u_v_robot_back))


def azimuthAngle(x1, y1, x2, y2):
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and y2 < y1:
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1:
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return dist


grid = 300
(__, frame) = camera.read()
height, width = frame.shape[:2]
h = [x for x in range(0, height+grid) if x % grid == 0]
w = [x for x in range(0, width+grid) if x % grid == 0]

# variable kecepatan
# requests.get(url+"2")
while True:

    # bola
    (__, frame) = camera.read()

    # frame = imutils.resize(frame, width=1280)

    # no_w = 8  # replace with no. of patches in width
    # no_h = 5  # replace with no. of patches in height
    # h, w = frame.shape[:2]
    # pixels_w = round(w/no_w)
    # pixels_h = round(h/no_h)
    # for i in range(0, h, pixels_h):
    #     cv2.line(frame, (0, i), (w, i), (0, 255, 0), 1)

    # for i in range(0, w, pixels_w):
    #     cv2.line(frame, (i, 0), (i, h), (0, 255, 0), 1)

    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    getTrackbarBola()

    lower_yellow = np.array([l_h_bola, l_s_bola, l_v_bola])
    upper_yellow = np.array([u_h_bola, u_s_bola, u_v_bola])
    mask_bola = cv2.inRange(hsv, lower_yellow, upper_yellow)

    mask_bola = cv2.erode(mask_bola, None, iterations=1)
    mask_bola = cv2.dilate(mask_bola, None, iterations=3)
    cnts_bola = cv2.findContours(mask_bola.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts_bola) > 0:
        c = max(cnts_bola, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)),
                       int(radius), (0, 255, 255), 2)
            for contour_bola in cnts_bola:
                area = cv2.contourArea(contour_bola)
                if(area > 1000):
                    M = cv2.moments(contour_bola)
                    if M['m00'] != 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                        x_bola = cx
                        y_bola = cy

    # robot depan
    getTrackbarRobotFront()
    lower_red = np.array([l_h_robot_front, l_s_robot_front, l_v_robot_front])
    upper_red = np.array([u_h_robot_front, u_s_robot_front, u_v_robot_front])
    mask_robot_front = cv2.inRange(hsv, lower_red, upper_red)

    mask_robot_front = cv2.erode(mask_robot_front, None, iterations=1)
    mask_robot_front = cv2.dilate(mask_robot_front, None, iterations=3)
    cnts_robot_front = cv2.findContours(mask_robot_front.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)[-2]

    for contour_robot_front in cnts_robot_front:
        area = cv2.contourArea(contour_robot_front)

        if(area > 1000):
            cv2.drawContours(frame,
                             contour_robot_front, -1, (0, 255, 0), 3)
            M = cv2.moments(contour_robot_front)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                x_robot_front = cx
                y_robot_back = cy

    # robot belakang
    getTrackbarRobotBack()

    lower_blue = np.array([l_h_robot_back, l_s_robot_back, l_v_robot_back])
    upper_blue = np.array([u_h_robot_back, u_s_robot_back, u_v_robot_back])
    mask_robot_back = cv2.inRange(hsv, lower_blue, upper_blue)

    mask_robot_back = cv2.erode(mask_robot_back, None, iterations=1)
    mask_robot_back = cv2.dilate(mask_robot_back, None, iterations=3)
    cnts_robot_back = cv2.findContours(mask_robot_back.copy(), cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)[-2]

    for contour_robot_back in cnts_robot_back:
        area = cv2.contourArea(contour_robot_back)

        if(area > 1000):
            cv2.drawContours(frame,
                             contour_robot_back, -1, (0, 255, 0), 3)
            M = cv2.moments(contour_robot_back)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                x_robot_back = cx
                y_robot_back = cy

    copy_frame = frame.copy()
    alpha = 0.3  # Transparency factor.

    for i in range(0, np.size(w, 0)-1):
        for j in range(0, np.size(h, 0)-1):
            print("1 : "+str((w[i], h[j])))
            print("2 : "+str((w[i+1], h[j+1])))
            if(i == 1 and j == 1):
                cv2.rectangle(copy_frame, (w[i], h[j]),
                              (w[i+1], h[j+1]), (0, 0, 255), -1)
            elif(i == 3 and j == 0):
                cv2.rectangle(copy_frame, (w[i], h[j]),
                              (w[i+1], h[j+1]), (0, 255, 0), -1)
            else:
                cv2.rectangle(frame, (w[i], h[j]),
                              (w[i+1], h[j+1]), (0, 255, 0), 1)

    frame = cv2.addWeighted(copy_frame, alpha, frame, 1 - alpha, 0)
    cv2.imshow("frame", frame)
    # cv2.imshow("mask_bola", mask_bola)
    # cv2.imshow("mask_robot_front", mask_robot_front)
    # cv2.imshow("mask_robot_back", mask_robot_back)

    azimuth_bola = azimuthAngle(x_robot_front, y_robot_front, x_bola, y_bola)
    distance = calculateDistance(x_robot_front, y_robot_front, x_bola, y_bola)

    # print("Azimuth : "+str(azimuth_bola))
    # print("Distance : "+str(distance))
    # print("Walk : "+str(walk))

    if(walk == 1):
        if(azimuth_bola):
            if ((azimuth_bola > 0 and azimuth_bola < 35) or (azimuth_bola < 360 and azimuth_bola > 330)):
                requests.get(url+"S")
            elif(azimuth_bola > 35 and azimuth_bola < 50):
                requests.get(url+"L")
            elif(azimuth_bola > 310 and azimuth_bola < 325):
                requests.get(url+"R")
            elif(azimuth_bola > 50 and azimuth_bola < 180):
                requests.get(url+"L")
            elif(azimuth_bola > 180 and azimuth_bola < 310):
                requests.get(url+"R")
    # else:
    #     requests.get(url+"S")

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        walk = 1

    if key == ord("d"):
        walk = 0

    if key == ord("q"):
        # requests.get(url+"S")
        break

camera.release()
cv2.destroyAllWindows()
